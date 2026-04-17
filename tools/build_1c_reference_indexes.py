from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"
INDEX_DIR = TOOLS_DIR / "reference_indexes"
SAMPLES_DIR = ROOT / "samples_1c"

LIBRARIES = {
    "unf": "УНФ",
    "bsp": "БСП",
}

SECTIONS = [
    "Catalogs",
    "Documents",
    "AccumulationRegisters",
    "InformationRegisters",
    "Reports",
    "HTTPServices",
    "WebServices",
    "CommonModules",
    "ChartsOfCharacteristicTypes",
    "DefinedTypes",
    "DataProcessors",
    "DocumentJournals",
    "Enums",
]

DEFAULT_SAMPLE_RULES = [
    ("subordinate_catalog", "Catalogs"),
    ("catalog_with_form", "Catalogs"),
    ("document", "Documents"),
    ("accumulation_register", "AccumulationRegisters"),
    ("information_register", "InformationRegisters"),
    ("report", "Reports"),
    ("http_service", "HTTPServices"),
    ("common_module", "CommonModules"),
    ("chart_of_characteristic_types", "ChartsOfCharacteristicTypes"),
]

OWNER_RE = re.compile(r"<xr:Item xsi:type=\"xr:MDObjectRef\">(.*?)</xr:Item>")
STANDARD_ATTR_RE = re.compile(r"<xr:StandardAttribute name=\"(.*?)\">")
DEFAULT_FORM_RE = {
    tag: re.compile(rf"<{tag}>(.*?)</{tag}>")
    for tag in ["DefaultObjectForm", "DefaultListForm", "DefaultChoiceForm"]
}


@dataclass
class ObjectInfo:
    name: str
    section: str
    xml: str
    owners: list[str]
    standard_attributes: list[str]
    has_standard_owner: bool
    default_forms: dict[str, str]
    forms: list[str]
    ext_files: list[str]

    @property
    def has_forms(self) -> bool:
        return bool(self.forms)

    @property
    def has_ext(self) -> bool:
        return bool(self.ext_files)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "section": self.section,
            "xml": self.xml,
            "owners": self.owners,
            "standard_attributes": self.standard_attributes,
            "has_standard_owner": self.has_standard_owner,
            "default_forms": self.default_forms,
            "forms": self.forms,
            "ext_files": self.ext_files,
        }


def rel_to_root(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_section_xml(lib_root: Path, section: str) -> Iterable[Path]:
    section_dir = lib_root / section
    if not section_dir.exists():
        return []
    return sorted(section_dir.glob("*.xml"))


def files_in(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(rel_to_root(p) for p in path.rglob("*") if p.is_file())


def extract_default_forms(xml_text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for tag, pattern in DEFAULT_FORM_RE.items():
        match = pattern.search(xml_text)
        if match and match.group(1).strip():
            result[tag] = match.group(1).strip()
    return result


def build_index(lib_root: Path) -> dict[str, list[ObjectInfo]]:
    index: dict[str, list[ObjectInfo]] = {}
    for section in SECTIONS:
        items: list[ObjectInfo] = []
        for xml_path in iter_section_xml(lib_root, section):
            text = read_text(xml_path)
            base_path = xml_path.with_suffix("")
            standard_attributes = STANDARD_ATTR_RE.findall(text)
            item = ObjectInfo(
                name=xml_path.stem,
                section=section,
                xml=rel_to_root(xml_path),
                owners=OWNER_RE.findall(text),
                standard_attributes=standard_attributes,
                has_standard_owner="Owner" in standard_attributes,
                default_forms=extract_default_forms(text),
                forms=files_in(base_path / "Forms"),
                ext_files=files_in(base_path / "Ext"),
            )
            items.append(item)
        index[section] = items
    return index


def pick_sample(index: dict[str, list[ObjectInfo]], sample_kind: str, section: str) -> ObjectInfo | None:
    items = index.get(section, [])
    if sample_kind == "subordinate_catalog":
        return next((i for i in items if i.owners and i.has_standard_owner), None)
    if sample_kind == "catalog_with_form":
        return next((i for i in items if i.has_forms), None)
    if sample_kind == "document":
        return next((i for i in items if i.has_forms or i.has_ext), None) or (items[0] if items else None)
    if sample_kind == "accumulation_register":
        return items[0] if items else None
    if sample_kind == "information_register":
        return items[0] if items else None
    if sample_kind == "report":
        return next((i for i in items if i.has_forms or i.has_ext), None) or (items[0] if items else None)
    if sample_kind == "http_service":
        return items[0] if items else None
    if sample_kind == "common_module":
        return next((i for i in items if i.has_ext), None) or (items[0] if items else None)
    if sample_kind == "chart_of_characteristic_types":
        return items[0] if items else None
    return items[0] if items else None


def copy_related_files(lib_root: Path, obj: ObjectInfo, dest_dir: Path) -> list[str]:
    copied: list[str] = []
    xml_source = ROOT / obj.xml
    relative_xml = Path(obj.xml).relative_to(lib_root.name)
    target_xml = dest_dir / relative_xml
    target_xml.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(xml_source, target_xml)
    copied.append(str(target_xml.relative_to(dest_dir)).replace("\\", "/"))

    base_path = xml_source.with_suffix("")
    for subdir_name in ["Forms", "Ext"]:
        source_subdir = base_path / subdir_name
        if not source_subdir.exists():
            continue
        for source_file in source_subdir.rglob("*"):
            if not source_file.is_file():
                continue
            relative_file = source_file.relative_to(lib_root)
            target_file = dest_dir / relative_file
            target_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, target_file)
            copied.append(str(target_file.relative_to(dest_dir)).replace("\\", "/"))
    return sorted(copied)


def build_samples(lib_key: str, lib_root: Path, index: dict[str, list[ObjectInfo]]) -> list[dict[str, object]]:
    dest_dir = SAMPLES_DIR / lib_key.upper()
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, object]] = []
    for sample_kind, section in DEFAULT_SAMPLE_RULES:
        selected = pick_sample(index, sample_kind, section)
        if selected is None:
            continue
        files = copy_related_files(lib_root, selected, dest_dir)
        manifest.append(
            {
                "sample_kind": sample_kind,
                "section": section,
                "object": selected.name,
                "source_xml": selected.xml,
                "files": files,
            }
        )
    return manifest


def build_markdown(title: str, lib_name: str, index: dict[str, list[ObjectInfo]], manifest: list[dict[str, object]]) -> str:
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"Быстрый индекс по библиотеке `{lib_name}`.")
    lines.append("")
    lines.append("## Как использовать")
    lines.append("")
    lines.append("1. Смотри `*.json`, если нужен машинный поиск по объектам.")
    lines.append("2. Смотри раздел `samples_1c`, если нужен компактный живой эталон без всей тяжелой конфигурации.")
    lines.append("3. Для подчиненных справочников проверяй поля `owners` и `has_standard_owner`.")
    lines.append("")
    lines.append("## Сводка")
    lines.append("")
    for section, items in index.items():
        if items:
            lines.append(f"- `{section}`: {len(items)} объектов")
    lines.append("")
    subordinate = [item for item in index.get("Catalogs", []) if item.owners]
    if subordinate:
        lines.append("## Подчиненные справочники")
        lines.append("")
        for item in subordinate[:25]:
            owners = ", ".join(item.owners)
            lines.append(f"- `{item.name}` -> `{owners}`; standard owner: `{item.has_standard_owner}`")
        lines.append("")
    lines.append("## Компактные эталоны")
    lines.append("")
    for entry in manifest:
        lines.append(f"- `{entry['sample_kind']}`: `{entry['object']}` ({entry['section']})")
    lines.append("")
    return "\n".join(lines)


def build_samples_markdown(all_manifests: dict[str, list[dict[str, object]]]) -> str:
    lines: list[str] = []
    lines.append("# samples_1c")
    lines.append("")
    lines.append("Компактные эталоны, собранные из тяжелых библиотек, чтобы не открывать их целиком каждый раз.")
    lines.append("")
    lines.append("## Что внутри")
    lines.append("")
    for lib_key, manifest in all_manifests.items():
        lines.append(f"- `{lib_key.upper()}`: {len(manifest)} эталонов")
    lines.append("")
    for lib_key, manifest in all_manifests.items():
        lines.append(f"## {lib_key.upper()}")
        lines.append("")
        for entry in manifest:
            files = ", ".join(f"`{path}`" for path in entry["files"][:6])
            lines.append(f"- `{entry['sample_kind']}` -> `{entry['object']}`: {files}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)

    all_manifests: dict[str, list[dict[str, object]]] = {}

    for lib_key, folder_name in LIBRARIES.items():
        lib_root = ROOT / folder_name
        if not lib_root.exists():
            raise SystemExit(f"Папка '{folder_name}' не найдена.")

        index = build_index(lib_root)
        json_path = INDEX_DIR / f"{lib_key}_index.json"
        md_path = INDEX_DIR / f"{lib_key}_index.md"
        json_path.write_text(
            json.dumps({k: [item.to_dict() for item in v] for k, v in index.items()}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        manifest = build_samples(lib_key, lib_root, index)
        all_manifests[lib_key] = manifest
        md_path.write_text(
            build_markdown(f"Индекс {folder_name}", folder_name, index, manifest),
            encoding="utf-8",
        )

    (SAMPLES_DIR / "README.md").write_text(build_samples_markdown(all_manifests), encoding="utf-8")
    print(f"Saved indexes to {INDEX_DIR}")
    print(f"Saved samples to {SAMPLES_DIR}")


if __name__ == "__main__":
    main()
