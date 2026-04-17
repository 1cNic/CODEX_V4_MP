from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "tools" / "reference_indexes"


def load_index(library: str) -> dict:
    path = INDEX_DIR / f"{library}_index.json"
    if not path.exists():
        raise SystemExit(f"Индекс не найден: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def matches(item: dict, query: str, section: str | None, owners_only: bool) -> bool:
    if section and item.get("section") != section:
        return False
    if owners_only and not item.get("owners"):
        return False
    if not query:
        return True

    haystacks = [
        item.get("name", ""),
        item.get("xml", ""),
        " ".join(item.get("owners", [])),
        " ".join(item.get("forms", [])),
        " ".join(item.get("ext_files", [])),
    ]
    query_lower = query.lower()
    return any(query_lower in hay.lower() for hay in haystacks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Быстрый поиск по индексам УНФ/БСП")
    parser.add_argument("query", nargs="?", default="", help="Подстрока для поиска")
    parser.add_argument("--library", choices=["unf", "bsp"], required=True)
    parser.add_argument("--section", help="Например Catalogs, Documents, Reports")
    parser.add_argument("--owners-only", action="store_true", help="Только объекты с владельцами")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    index = load_index(args.library)
    results: list[dict] = []
    for section_name, items in index.items():
        for item in items:
            item = dict(item)
            item["section"] = section_name
            if matches(item, args.query, args.section, args.owners_only):
                results.append(item)

    for item in results[: args.limit]:
        owners = ", ".join(item.get("owners", [])) or "-"
        print(f"[{item['section']}] {item['name']}")
        print(f"  xml: {item['xml']}")
        print(f"  owners: {owners}")
        if item.get("default_forms"):
            print(f"  default_forms: {item['default_forms']}")
        if item.get("forms"):
            print(f"  forms: {len(item['forms'])}")
        if item.get("ext_files"):
            print(f"  ext: {len(item['ext_files'])}")
    print(f"Всего найдено: {len(results)}")


if __name__ == "__main__":
    main()
