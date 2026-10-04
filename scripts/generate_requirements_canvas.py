#!/usr/bin/env python3
"""Generate focused Epic or Feature Canvases from requirement metadata."""

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


PROJECTS_ROOT = Path("Notes/pjs")
RELATIONSHIPS = {"epic", "feature", "story", "next_story"}
SCALARS = {
    "id",
    "project",
    "epic",
    "feature",
    "story",
    "next_story",
    "transition",
    "transition_color",
}
KINDS = {"epic", "feature", "story", "acceptance-criteria"}


@dataclass(frozen=True)
class Note:
    path: Path
    identifier: str
    kind: str
    title: str
    properties: dict[str, str]


def fail(message: str) -> None:
    raise SystemExit(message)


def normalize_reference(value: str) -> str:
    value = value.strip().strip("\"'")
    if value.startswith("[[") and value.endswith("]]" ):
        value = value[2:-2].split("|", 1)[0].split("#", 1)[0]
    return value.strip()


def stable_id(kind: str, value: str) -> str:
    return hashlib.sha256(f"{kind}:{value}".encode()).hexdigest()[:16]


def frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"Missing YAML frontmatter: {path}")

    values: dict[str, str] = {}
    current_list = ""
    for raw in parts[1].splitlines():
        if raw.startswith((" ", "\t")):
            item = raw.strip()
            if current_list == "type" and item.startswith("-"):
                values["type"] = item[1:].strip().strip("\"'")
            continue
        current_list = ""
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip(), value.strip()
        if key == "type" and not value:
            current_list = "type"
        elif key == "type" or key in SCALARS:
            values[key] = (
                normalize_reference(value)
                if key in RELATIONSHIPS
                else value.strip("\"'")
            )
    return values, parts[2]


def read_note(path: Path) -> Note:
    values, body = frontmatter(path.read_text(encoding="utf-8"), path)
    identifier = values.get("id", "")
    kind = values.get("type", "").lower()
    if not identifier:
        fail(f"Missing id property: {path}")
    if kind not in KINDS:
        fail(f"Unsupported or missing type in {path}: {kind or 'missing'}")
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    title = heading.group(1) if heading else identifier
    return Note(path, identifier, kind, title, values)


def load_notes(root: Path) -> list[Note]:
    notes = []
    for path in sorted(root.rglob("*.md")):
        try:
            notes.append(read_note(path))
        except SystemExit:
            continue
    identifiers = [note.identifier for note in notes]
    duplicates = sorted(
        identifier
        for identifier in set(identifiers)
        if identifiers.count(identifier) > 1
    )
    if duplicates:
        fail(f"Duplicate requirement IDs: {', '.join(duplicates)}")
    return notes


def requirement_root(note: Note) -> Path:
    for parent in note.path.parents:
        if parent.name == "reqs" and parent.parent.name == "docs":
            return parent
    fail(f"Note is not under <project>/docs/reqs: {note.path}")


def file_node(
    note: Note,
    repository: Path,
    x: int,
    y: int,
    color: str,
) -> dict[str, object]:
    return {
        "id": stable_id("node", note.path.as_posix()),
        "type": "file",
        "file": note.path.relative_to(repository).as_posix(),
        "x": x,
        "y": y,
        "width": 300,
        "height": 180,
        "color": color,
    }


def group_node(
    key: str,
    label: str,
    x: int,
    y: int,
    width: int,
    height: int,
    color: str,
) -> dict[str, object]:
    return {
        "id": stable_id("group", key),
        "type": "group",
        "label": label,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "color": color,
    }


def edge(
    source: Note,
    target: Note,
    label: str | None = None,
    color: str | None = None,
) -> dict[str, object]:
    result: dict[str, object] = {
        "id": stable_id(
            "edge",
            f"{source.identifier}:{target.identifier}:{label or ''}",
        ),
        "fromNode": stable_id("node", source.path.as_posix()),
        "fromSide": "right",
        "toNode": stable_id("node", target.path.as_posix()),
        "toSide": "left",
        "toEnd": "arrow",
    }
    if label:
        result["label"] = label
    if color:
        result["color"] = color
    return result


def build_feature_canvas(
    feature: Note,
    notes: list[Note],
    repository: Path,
) -> dict[str, list[dict[str, object]]]:
    epic_id = feature.properties.get("epic", "")
    epic = next(
        (
            note
            for note in notes
            if note.identifier == epic_id and note.kind == "epic"
        ),
        None,
    )
    if epic is None:
        fail(
            f"Feature {feature.identifier} has no resolvable Epic: "
            f"{epic_id or 'missing'}"
        )

    stories = sorted(
        (
            note
            for note in notes
            if note.kind == "story"
            and note.properties.get("feature") == feature.identifier
        ),
        key=lambda note: note.identifier,
    )
    criteria = sorted(
        (
            note
            for note in notes
            if note.kind == "acceptance-criteria"
            and note.properties.get("feature") == feature.identifier
        ),
        key=lambda note: note.identifier,
    )
    height = max(260, 230 * max(len(stories), len(criteria)))
    nodes = [
        group_node(
            f"{feature.identifier}:hierarchy",
            "Epic and Feature",
            -40,
            -40,
            740,
            260,
            "5",
        ),
        group_node(
            f"{feature.identifier}:delivery",
            "Stories and Acceptance Criteria",
            760,
            -40,
            760,
            height,
            "3",
        ),
        file_node(epic, repository, 0, 0, "5"),
        file_node(feature, repository, 360, 0, "3"),
    ]
    edges = [edge(epic, feature)]
    stories_by_id = {note.identifier: note for note in stories}

    for index, story in enumerate(stories):
        nodes.append(file_node(story, repository, 800, index * 230, "4"))
        edges.append(edge(feature, story))

    for index, criterion in enumerate(criteria):
        nodes.append(
            file_node(criterion, repository, 1180, index * 230, "6")
        )
        story = stories_by_id.get(criterion.properties.get("story", ""))
        if story:
            edges.append(edge(story, criterion))

    for story in stories:
        target = stories_by_id.get(
            story.properties.get("next_story", "")
        )
        if target:
            edges.append(
                edge(
                    story,
                    target,
                    story.properties.get("transition"),
                    story.properties.get("transition_color"),
                )
            )
    return {"nodes": nodes, "edges": edges}


def build_epic_canvas(
    epic: Note,
    notes: list[Note],
    repository: Path,
) -> dict[str, list[dict[str, object]]]:
    features = sorted(
        (
            note
            for note in notes
            if note.kind == "feature"
            and note.properties.get("epic") == epic.identifier
        ),
        key=lambda note: note.identifier,
    )
    nodes = [
        group_node(
            f"{epic.identifier}:overview",
            "Epic and Features",
            -40,
            -40,
            760,
            max(260, 230 * len(features)),
            "5",
        ),
        file_node(epic, repository, 0, 0, "5"),
    ]
    edges = []
    for index, feature in enumerate(features):
        nodes.append(
            file_node(feature, repository, 380, index * 230, "3")
        )
        edges.append(edge(epic, feature))
    return {"nodes": nodes, "edges": edges}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_id")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repository = Path.cwd()
    projects_root = repository / PROJECTS_ROOT
    if not projects_root.is_dir():
        fail(f"Project root does not exist: {PROJECTS_ROOT}")

    notes = load_notes(projects_root)
    matches = [
        note for note in notes if note.identifier == args.artifact_id
    ]
    if len(matches) != 1:
        fail(
            f"Expected one artifact with ID {args.artifact_id}; "
            f"found {len(matches)}"
        )
    artifact = matches[0]
    if artifact.kind not in {"epic", "feature"}:
        fail(
            "Artifact must be an Epic or Feature; "
            f"found {artifact.kind}"
        )

    output = args.output or (
        requirement_root(artifact)
        / "canvases"
        / f"{artifact.identifier}-trace.generated.canvas"
    )
    if not output.name.endswith(".generated.canvas"):
        fail("Output filename must end with .generated.canvas")
    if output.exists() and not args.force:
        fail(f"Output exists; use --force: {output}")

    output.parent.mkdir(parents=True, exist_ok=True)
    if artifact.kind == "feature":
        canvas = build_feature_canvas(artifact, notes, repository)
    else:
        canvas = build_epic_canvas(artifact, notes, repository)
    output.write_text(
        json.dumps(canvas, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Generated {output} "
        f"({len(canvas['nodes'])} nodes, {len(canvas['edges'])} edges)"
    )


if __name__ == "__main__":
    main()
