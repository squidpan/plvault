#!/usr/bin/env python3
"""Tests for the focused requirements-template validator."""

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_requirements_templates.py"
SPEC = importlib.util.spec_from_file_location(
    "requirements_template_validator",
    VALIDATOR,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load validator")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RequirementsTemplateValidatorTests(unittest.TestCase):
    def test_current_focused_package_is_valid(self) -> None:
        self.assertEqual([], MODULE.validate())

    def test_singular_bavault_template_names_are_governed(self) -> None:
        self.assertEqual(
            {
                "Epic Template.md",
                "Feature Template.md",
                "User Story Template.md",
                "Acceptance Criteria Template.md",
            },
            set(MODULE.TEMPLATES),
        )

    def test_plural_template_names_are_rejected(self) -> None:
        self.assertEqual(
            {
                "Epics Template.md",
                "Features Template.md",
                "User Stories Template.md",
            },
            MODULE.LEGACY_TEMPLATES,
        )


if __name__ == "__main__":
    unittest.main()
