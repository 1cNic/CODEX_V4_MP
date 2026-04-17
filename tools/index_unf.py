from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
UNF_DIR = ROOT / "УНФ"
OUT_JSON = ROOT / "tools" / "unf_index.json"
OUT_MD = ROOT / "tools" / "unf_index.md"

SECTIONS = [
    "Catalogs",
    "Documents",
    "AccumulationRegisters",
    "InformationRegisters",
    "Reports",
    "HTTPServices",
    "CommonModules",
    "ChartsOfCharacteristicTypes",
    "DefinedTypes",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_forms(base_path: Path) -> list[str]:
    forms_dir = base_path / "Forms"
    if not forms_dir.exists():
        return []
    return sorted(
        str(p.relative_to(ROOT)).replace("\\", "/")
        for p in forms_dir.rglob("*")
        if p.is_file()
    )


def find_ext_files(base_path: Path) -> list[str]:
    ext_dir = base_path / "Ext"
    if not ext_dir.exists():
        return []
    return sorted(
        str(p.relative_to(ROOT)).replace("\\", "/")
        for p in ext_dir.rglob("*")
        if p.is_file()
    )


def extract_owners(xml_text: str) -> list[str]:
    return re.findall(r"<xr:Item xsi:type=\"xr:MDObjectRef\">(.*?)</xr:Item>", xml_text)


def has_standard_owner(xml_text: str) -> bool:
    return '<xr:StandardAttribute name="Owner">' in xml_text


def extract_default_forms(xml_text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for tag in ["DefaultObjectForm", "DefaultListForm", "DefaultChoiceForm"]:
        match = re.search(rf"<{tag}>(.*?)</{tag}>", xml_text)
        if match and match.group(1).strip():
            result[tag] = match.group(1).strip()
    return result


def iter_section_xml(section: str) -> Iterable[Path]:
    section_dir = UNF_DIR / section
    if not section_dir.exists():
        return []
    return sorted(section_dir.glob("*.xml"))


def build_index() -> dict:
    index: dict[str, list[dict]] = {}
    for section in SECTIONS:
        items: list[dict] = []
        for xml_path in iter_section_xml(section):
            text = read_text(xml_path)
            object_name = xml_path.stem
            base_path = xml_path.with_suffix("")
            item = {
                "name": object_name,
                "section": section,
                "xml": str(xml_path.relative_to(ROOT)).replace("\\", "/"),
                "owners": extract_owners(text),
                "has_standard_owner": has_standard_owner(text),
                "default_forms": extract_default_forms(text),
                "forms": find_forms(base_path),
                "ext_files": find_ext_files(base_path),
            }
            items.append(item)
        index[section] = items
    return index


def build_markdown(index: dict) -> str:
    lines: list[str] = []
    lines.append("# УНФ быстрый индекс")
    lines.append("")
    lines.append("Файл сгенерирован скриптом `tools/index_unf.py`.")
    lines.append("")
    lines.append("## Как использовать")
    lines.append("")
    lines.append("1. Открыть `tools/unf_index.json` для машинного поиска по объектам.")
    lines.append("2. Искать по имени объекта, наличию владельцев, форм и модулей.")
    lines.append("3. Для подчиненных справочников смотреть поля `owners` и `has_standard_owner`.")
    lines.append("")
    lines.append("## Подчиненные справочники")
    lines.append("")
    for item in index.get("Catalogs", []):
        if item["owners"]:
            lines.append(f"- `{item['name']}`")
            lines.append(f"  xml: `{item['xml']}`")
            lines.append(f"  owners: `{', '.join(item['owners'])}`")
            lines.append(f"  standard owner attr: `{item['has_standard_owner']}`")
    lines.append("")
    lines.append("## Разделы")
    lines.append("")
    for section, items in index.items():
        lines.append(f"- `{section}`: {len(items)} объектов")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    if not UNF_DIR.exists():
        raise SystemExit("Папка 'УНФ' не найдена.")

    index = build_index()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(build_markdown(index), encoding="utf-8")
    print(f"Saved {OUT_JSON}")
    print(f"Saved {OUT_MD}")


if __name__ == "__main__":
    main()
