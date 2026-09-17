#!/usr/bin/env python3
"""Validate Starter Pack Markdown front matter, IDs, and local wiki links."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALID_TYPES = {
    "epic", "feature", "story", "acceptance-criteria", "business-rule",
    "data-element", "interface", "decision", "risk", "test-case",
    "discovery-note", "lineage", "mapping", "review",
}
REQUIRED = ("id", "project", "type", "status", "title", "description", "classification")
WIKI = re.compile(r"\[\[([^\]|#]+)")


def front_matter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    try:
        raw = text.split("---\n", 2)[1]
        data = yaml.safe_load(raw)
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"invalid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("front matter must be a mapping")
    return data


def main() -> int:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    notes = list(ROOT.rglob("*.md"))
    for path in notes:
        try:
            data = front_matter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        if data is None:
            continue
        for field in REQUIRED:
            if field not in data or data[field] in (None, ""):
                errors.append(f"{path.relative_to(ROOT)}: missing {field}")
        artifact_id = str(data.get("id", ""))
        if artifact_id:
            if artifact_id in ids:
                errors.append(f"duplicate ID {artifact_id}: {ids[artifact_id]} and {path}")
            ids[artifact_id] = path
        if data.get("type") not in VALID_TYPES:
            errors.append(f"{path.relative_to(ROOT)}: invalid type {data.get('type')!r}")
        if data.get("classification") != "synthetic-training":
            errors.append(f"{path.relative_to(ROOT)}: classification must be synthetic-training")

    filenames = {p.stem for p in notes}
    ignored_prefixes = ("FR-", "NFR-", "AC-RCE-101-0")
    for path in notes:
        for target in WIKI.findall(path.read_text(encoding="utf-8")):
            if "..." in target or "{{" in target:
                continue
            if target in filenames or target.startswith(ignored_prefixes):
                continue
            errors.append(f"{path.relative_to(ROOT)}: unresolved wiki link [[{target}]]")

    print(f"Markdown files: {len(notes)}; front-matter artifacts: {len(ids)}")
    if errors:
        print(f"Validation FAILED with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation PASS: YAML, IDs, classifications, types, and local wiki links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
