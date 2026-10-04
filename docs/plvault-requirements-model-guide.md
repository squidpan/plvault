# plvault requirements model guide

This focused model aligns plvault's reusable Epic, Feature, User Story, and
Acceptance Criteria architecture with bavault v0.2.0. It does not import
bavault's RIE content or its broader eighteen-template validation package.

## Project-note location

Store each project's requirement notes under:

`Notes/pjs/<project>/docs/reqs/`

Recommended folders are `epics`, `features`, `stories`,
`acceptance-criteria`, and `canvases`. Keep filenames descriptive and stable;
relationships resolve through YAML IDs rather than filenames.

## Canonical template names

Use the singular bavault v0.2.0 filenames:

- `Templates/Epic Template.md`
- `Templates/Feature Template.md`
- `Templates/User Story Template.md`
- `Templates/Acceptance Criteria Template.md`

The category-note names remain plural because they represent collections:
Epics, Features, Stories, Acceptance Criteria, and Requirements.

The former debt-issuance examples remain available under
`_jick/farm-credit-ba-exercise/docs/requirements/`; they are no longer baked
into reusable templates.

## Metadata contract

All four artifact types use `id`, `project`, `organization`, list-valued
`type`, `status`, `classification`, `description`, `categories`, `tags`,
`created`, and `last`. Dates use quoted Obsidian template placeholders.
`source_artifact` is optional and records provenance when it matters.

Use parent relationships as follows:

| Artifact | Required relationships |
| --- | --- |
| Epic | None |
| Feature | `epic` |
| User Story | `epic`, `feature` |
| Acceptance Criteria | `epic`, `feature`, `story` |

Values may be plain IDs or wikilinks. Plain IDs are the simplest convention.
The hierarchy can stop at the level that adds value; a small project should
not invent extra levels merely to fill the model.

Story flow is optional. Add `next_story`, `transition`, and
`transition_color` only when sequence or branching improves the Canvas.

## Property compatibility

plvault is a compatible superset of bavault. Existing personal, artwork, and
media registrations remain intact. Every shared BA property uses the same
Obsidian property type as bavault v0.2.0.

## Bases

`Templates/Bases/Requirements.base` searches `Notes/pjs` and provides All
Requirements, Epics, Features, Stories, and Acceptance Criteria views.

`Templates/Bases/Reference Exercises.base` uses the same bavault navigation
shape but searches plvault's existing `References` root instead of
`References/repos`.

## Canvas generation

Generate a disposable Feature or Epic navigation Canvas from the vault root:

    python3.13 scripts/generate_requirements_canvas.py FE-PROJECT-001
    python3.13 scripts/generate_requirements_canvas.py EPIC-PROJECT-001

Generated filenames always end with `.generated.canvas`; the tool refuses to
overwrite curated Canvas names. Use `--force` only to replace an existing
generated view.

Obsidian Canvas groups are spatial containers rather than a true nested
hierarchy. Apparent nesting is produced through coordinated group and card
layout.

## Verification

Run from the vault root:

    python3.13 scripts/validate_requirements_templates.py
    python3.13 -m unittest discover -s tests -p 'test_*requirements*.py' -v
    git diff --check

Delete generated Canvases after comparison unless they are deliberately being
retained as reproducible working views.
