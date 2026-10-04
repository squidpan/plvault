#!/usr/bin/env python3
"""Tests for the focused metadata-driven requirements Canvas generator."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts/generate_requirements_canvas.py"
SPEC = importlib.util.spec_from_file_location(
    "requirements_canvas_generator",
    GENERATOR,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load generator")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RequirementsCanvasGeneratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.reqs = self.root / "Notes/pjs/demo/docs/reqs"
        for folder in (
            "epics",
            "features",
            "stories",
            "acceptance-criteria",
        ):
            (self.reqs / folder).mkdir(parents=True, exist_ok=True)

        notes = {
            "epics/EP-DEMO-001.md": (
                "EP-DEMO-001",
                "epic",
                "",
                "Demo Epic",
            ),
            "features/FE-DEMO-001.md": (
                "FE-DEMO-001",
                "feature",
                "epic: EP-DEMO-001",
                "Demo Feature",
            ),
            "stories/US-DEMO-001.md": (
                "US-DEMO-001",
                "story",
                "epic: EP-DEMO-001\n"
                "feature: FE-DEMO-001\n"
                "next_story: US-DEMO-002\n"
                "transition: then",
                "First Story",
            ),
            "stories/US-DEMO-002.md": (
                "US-DEMO-002",
                "story",
                "epic: EP-DEMO-001\nfeature: FE-DEMO-001",
                "Second Story",
            ),
            "acceptance-criteria/AC-DEMO-001.md": (
                "AC-DEMO-001",
                "acceptance-criteria",
                "epic: EP-DEMO-001\n"
                "feature: FE-DEMO-001\n"
                "story: US-DEMO-001",
                "First Criteria",
            ),
        }
        for relative, values in notes.items():
            identifier, kind, relationships, title = values
            (self.reqs / relative).write_text(
                "---\n"
                f"id: {identifier}\n"
                "type:\n"
                f"  - {kind}\n"
                f"{relationships}\n"
                "---\n\n"
                f"# {title}\n",
                encoding="utf-8",
            )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_generator(
        self,
        identifier: str,
        output: Path,
        *extra: str,
        check: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(GENERATOR),
                identifier,
                "--output",
                str(output),
                *extra,
            ],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=check,
        )

    def test_list_type_and_wikilink_are_parsed(self) -> None:
        path = self.reqs / "features/FE-DEMO-002.md"
        path.write_text(
            "---\n"
            "id: FE-DEMO-002\n"
            "type:\n"
            "  - feature\n"
            'epic: "[[EP-DEMO-001]]"\n'
            "---\n"
            "# Two\n",
            encoding="utf-8",
        )
        note = MODULE.read_note(path)
        self.assertEqual("feature", note.kind)
        self.assertEqual("EP-DEMO-001", note.properties["epic"])

    def test_feature_canvas_has_hierarchy_and_workflow(self) -> None:
        output = self.root / "FE-DEMO-001-trace.generated.canvas"
        self.run_generator("FE-DEMO-001", output)
        canvas = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(7, len(canvas["nodes"]))
        self.assertEqual(5, len(canvas["edges"]))
        labels = {edge.get("label") for edge in canvas["edges"]}
        self.assertIn("then", labels)

    def test_epic_canvas_is_deterministic(self) -> None:
        output = self.root / "EP-DEMO-001-trace.generated.canvas"
        self.run_generator("EP-DEMO-001", output)
        first = output.read_bytes()
        self.run_generator("EP-DEMO-001", output, "--force")
        self.assertEqual(first, output.read_bytes())

    def test_curated_output_name_is_rejected(self) -> None:
        output = self.root / "EP-DEMO-001-trace.canvas"
        result = self.run_generator(
            "EP-DEMO-001",
            output,
            check=False,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn(".generated.canvas", result.stderr)


if __name__ == "__main__":
    unittest.main()
