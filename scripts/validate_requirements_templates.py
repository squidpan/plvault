#!/usr/bin/env python3
"""Validate the focused plvault Epic/Feature/Story/AC template contract."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = {
    "Epic Template.md": ("epic", []),
    "Feature Template.md": ("feature", ["epic"]),
    "User Story Template.md": ("story", ["epic", "feature"]),
    "Acceptance Criteria Template.md": (
        "acceptance-criteria",
        ["epic", "feature", "story"],
    ),
}
LEGACY_TEMPLATES = {
    "Epics Template.md",
    "Features Template.md",
    "User Stories Template.md",
}
REQUIRED_PROPERTIES = {
    "id": "text",
    "project": "text",
    "organization": "text",
    "type": "multitext",
    "status": "multitext",
    "classification": "text",
    "description": "text",
    "epic": "text",
    "feature": "text",
    "story": "text",
    "source_artifact": "text",
}


def frontmatter(path: Path) -> str:
    parts = path.read_text(encoding="utf-8").split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Missing YAML frontmatter: {path}")
    return parts[1]


def validate() -> list[str]:
    errors = []
    templates_root = ROOT / "Templates"

    for filename in sorted(LEGACY_TEMPLATES):
        if (templates_root / filename).exists():
            errors.append(f"Legacy plural template remains: {filename}")

    for filename, (kind, parents) in TEMPLATES.items():
        path = templates_root / filename
        if not path.is_file():
            errors.append(f"Missing template: {filename}")
            continue
        yaml = frontmatter(path)
        checks = {
            "generic ID placeholder": "id: REPLACE-WITH-" in yaml,
            "project": "project: REPLACE-WITH-PROJECT-ID" in yaml,
            "organization": (
                "organization: REPLACE-WITH-ORGANIZATION" in yaml
            ),
            "list-valued type": bool(
                re.search(
                    rf"(?m)^type:\s*$\n\s+- {re.escape(kind)}$",
                    yaml,
                )
            ),
            "classification": (
                "classification: REPLACE-WITH-CLASSIFICATION" in yaml
            ),
            "quoted created date": 'created: "{{date}}"' in yaml,
            "quoted last date": 'last: "{{date}}"' in yaml,
            "optional source": (
                "# source_artifact: REPLACE-WITH-SOURCE-PATH" in yaml
            ),
        }
        for parent in parents:
            checks[f"parent {parent}"] = bool(
                re.search(
                    rf"(?m)^{parent}: REPLACE-WITH-",
                    yaml,
                )
            )
        for label, passed in checks.items():
            if not passed:
                errors.append(f"{filename}: missing or invalid {label}")

        text = path.read_text(encoding="utf-8")
        if re.search(
            r"(?i)debt|issuance officer|farm-credit",
            text,
        ):
            errors.append(
                f"{filename}: domain-specific example remains"
            )

    types = json.loads(
        (ROOT / ".obsidian/types.json").read_text(encoding="utf-8")
    )["types"]
    for name, expected in REQUIRED_PROPERTIES.items():
        if types.get(name) != expected:
            errors.append(
                f"Property {name}: expected {expected}; "
                f"found {types.get(name, 'missing')}"
            )

    required_files = {
        "Templates/Bases/Requirements.base",
        "Templates/Bases/Reference Exercises.base",
        "Categories/Epics.md",
        "Categories/Features.md",
        "Categories/Stories.md",
        "Categories/Acceptance Criteria.md",
        "Categories/Requirements.md",
        "Categories/Reference Exercises.md",
    }
    for relative in sorted(required_files):
        if not (ROOT / relative).is_file():
            errors.append(f"Missing navigation file: {relative}")

    return errors


def main() -> None:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("Focused requirements-template validation PASS")
    print(f"Templates: {len(TEMPLATES)}")
    print(f"Required property registrations: {len(REQUIRED_PROPERTIES)}")
    print("Legacy plural templates: none")


if __name__ == "__main__":
    main()
