# Requirements Layout Design Handoff

## Obsidian-Native Epic Visual Requirements Workflow

### Purpose

This note summarizes the architectural decision reached while evaluating Base44 and Claude Code for the BibleProject-inspired requirements-layout experiment. It should be brought back into the **Jobs** project chat **“Requirements Layout Design.”**

The immediate objective is to prepare for the Fidelity **Rep Code Expansion** Business Analyst work by developing a reusable way to represent an Epic as a visual story. The Genesis one-page summary remains the reference model for learning and proving the method.

## Core Decision

The primary product should be an **Obsidian-native visual requirements generator**, not a Base44 application.

The intended workflow is:

1. Create real Markdown notes for Epics, Features, Stories, Acceptance Criteria, business rules, decisions, risks, flows, and supporting evidence.
2. Use YAML properties and Markdown wikilinks to describe relationships among those artifacts.
3. Dynamically generate an initial Obsidian Canvas from the notes.
4. Apply the Genesis/BibleProject visual structure to organize the generated material.
5. Generate an initial Excalidraw composition or use an Excalidraw layout template.
6. Refine the executive-level visual synthesis manually in Obsidian Excalidraw.

The map must reference the **actual notes**. It must not become a disconnected copy of requirement text.

## Tool Responsibilities

### Obsidian Markdown — Source of Truth

Obsidian Markdown notes hold the actual requirements and analysis. The canonical hierarchy remains:

```text
Epic
└── Feature
    └── Story
        ├── Acceptance Criteria
        ├── Business Rules
        ├── Validation
        ├── Dependencies
        └── Related Artifacts
```

Acceptance Criteria remain separate artifacts and are directly linked, for example `[[AC-RCE-101-01]]`. They should not be buried in an unstructured Notes section.

### Obsidian Canvas — Generated Working Map

Canvas should provide the dynamically assembled, linked working view. A generator can scan the notes and create:

- File nodes that open the real Markdown notes.
- Groups for narrative regions, phases, workstreams, and system boundaries.
- Edges derived from parent, dependency, related-artifact, and flow relationships.
- Initial coordinates based on the Genesis layout.
- Colors based on artifact type or narrative function.
- A repeatable starting point that can be regenerated as the notes evolve.

### Obsidian Excalidraw — Curated Visual Synthesis

Excalidraw supplies the richer visual grammar that Canvas alone cannot provide:

- Curved and hand-drawn arrows.
- Labeled frames and boundary boxes.
- Bubbles, icons, and recurring motifs.
- A broad problem/escalation region.
- A visually dominant central hinge.
- Narrower transformation streams.
- Resolution and open-dependency regions.
- Manual control over the final one-page composition.

The Excalidraw result is the highest-level synthesis of the underlying research and requirements. It is not a replacement for the detailed notes.

## Genesis Narrative Structure

The existing Genesis structure should become the reusable visual grammar:

| Region | Genesis function | Requirements equivalent |
|---|---|---|
| `REG-01 THE POINT` | Governing thesis | Epic objective and business outcome |
| `REG-10 TRIGGERING TENSION` | Initial disruption | Business problem or initiating condition |
| `REG-11 ESCALATING EVIDENCE` | Recurring failure | Pain points, incidents, gaps, and risks |
| `REG-12 ACT I SYNTHESIS` | Conclusion of the problem movement | Current-state or gap-analysis conclusion |
| `REG-20 THE HINGE` | Genesis 12:1–3 intervention | Key decision, transformation, or architectural intervention |
| `REG-30A–C TRANSFORMATION STREAMS` | Abraham-family movements | Features, capabilities, or delivery workstreams |
| `REG-31 PERSISTENT PATTERNS` | Repeated unresolved patterns | Cross-cutting rules, constraints, and risks |
| `REG-41 RESOLUTION` | Partial resolution | Target state and measurable outcomes |
| `REG-42 OPEN DEPENDENCIES` | Continuation into Exodus | Dependencies, unresolved questions, and roadmap |

The reveal flow remains:

```text
orientation
→ baseline
→ actors and purpose
→ governing tension
→ trigger
→ first-order impacts
→ escalating evidence and pattern
→ synthesis
→ unresolved question
→ hinge
→ transformation
→ resolution
→ open dependency
```

## Proposed Note Metadata

Each artifact needs structured metadata that identifies both its requirements role and its narrative role.

Example:

```yaml
---
id: US-RCE-101
type: story
title: Resolve four-character rep code
epic: EPIC-RCE-001
feature: FEATURE-RCE-010
narrative_role: transformation
stream: translation
sequence: 20
status: discovery
priority: high
systems:
  - New Trading Platform
  - Legacy Trading System
related:
  - AC-RCE-101-01
  - BR-RCE-020
  - RISK-RCE-007
---
```

Possible `narrative_role` values include:

```text
point
baseline
tension
evidence
synthesis
hinge
transformation
persistent_pattern
resolution
open_dependency
```

This additional classification allows the generator to create a visual argument instead of merely arranging requirement cards.

## Rep Code Expansion Application

The Rep Code Expansion Epic can reuse the Genesis structure directly:

| Narrative region | Rep Code Expansion content |
|---|---|
| Point | Expand rep-code capacity while preserving correct and auditable processing |
| Tension | New four-character identifier conflicts with three-character legacy constraints |
| Escalating evidence | Interface gaps, validation failures, mapping gaps, and silent truncation risk |
| Act I synthesis | Storage changes alone do not provide end-to-end compatibility |
| Hinge | Centralized controlled mapping and translation capability |
| Transformation streams | Translation, validation, exception handling, lineage, rollout, and controls |
| Persistent patterns | Legacy constraints and cross-system data-quality risks |
| Resolution | Correct, controlled, traceable, and auditable processing |
| Open dependencies | Remaining systems, rollout waves, unresolved decisions, and roadmap |

This makes the Genesis exercise practical preparation for the job rather than a separate illustration project.

## Generation and Manual Refinement

Automatic generation and manual visual refinement must coexist without one destroying the other.

Recommended artifact lifecycle:

```text
rep-code-expansion.generated.canvas
rep-code-expansion.seed-v001.excalidraw.md
rep-code-expansion-curated-v001.excalidraw.md
```

Recommended workflow:

1. Update the Markdown requirement notes.
2. Run the generator.
3. Regenerate the live Canvas.
4. Generate a new versioned Excalidraw seed when needed.
5. Promote or copy useful changes into the curated Excalidraw artifact.
6. Continue manual refinement in the curated version.

The generator should never overwrite the manually curated Excalidraw file. Preserve previous visual artifacts and create revised versions alongside them.

This avoids fragile two-way synchronization:

- **Canvas is the regeneratable, live requirements map.**
- **Excalidraw is the deliberately curated executive synthesis.**

## Potential Generator Components

A future local tool could contain:

```text
scripts/
├── scan_requirements.py
├── validate_frontmatter.py
├── build_epic_manifest.py
├── generate_canvas.py
├── generate_excalidraw_seed.py
└── generate_traceability_report.py
```

The tooling should eventually:

- Read Obsidian Markdown and YAML.
- Resolve wikilinks.
- Validate required IDs and properties.
- Detect broken links, missing parents, and orphaned artifacts.
- Build Canvas nodes, groups, edges, and initial coordinates.
- Place artifacts into Genesis-style narrative regions.
- Produce a versioned Excalidraw seed.
- Generate traceability and coverage reports.

## Base44 and Claude Code Decision

### Claude Code

Claude Code may later be useful for developing the local generator and maintaining its scripts, schemas, validation, and tests. No Claude Code implementation is being started in this phase.

### Base44

Base44 is deferred. It may eventually publish the same structured requirements as an interactive browser-based Epic explorer, but it should not become a second source of truth or be introduced before the Obsidian model is stable.

Before returning to Base44, stabilize:

- The Markdown note schema.
- Artifact identifiers and wikilinks.
- Narrative roles.
- Canvas generation rules.
- Genesis layout regions.
- Excalidraw seed and curation workflow.
- Regeneration and versioning behavior.

## Recommended Project Progression

```text
Genesis storyboard
→ Genesis note and metadata model
→ Generated Genesis Canvas
→ Curated Genesis Excalidraw one-pager
→ Method v0.1
→ Rep Code Expansion content model
→ Generated Rep Code Expansion Canvas
→ Curated Rep Code Expansion one-pager
→ Optional Claude Code implementation work
→ Optional Base44 interactive publishing experiment
```

## Immediate Next Deliverable in “Requirements Layout Design”

Define an **Epic Visual Requirements Generator v0.1 specification** covering:

1. Vault and folder structure.
2. Artifact naming and ID conventions.
3. YAML schema for each artifact type.
4. Wikilink and relationship conventions.
5. Narrative-role definitions.
6. Genesis layout manifest.
7. Canvas node, group, edge, and positioning rules.
8. Excalidraw seed-template rules.
9. Manual-curation and versioning workflow.
10. Validation and traceability requirements.

## Current Status

No Base44 or Claude Code build should begin yet. Continue the design and Genesis prototype work in **“Requirements Layout Design.”** Return to the Base44/Claude Code discussion after the Obsidian-native model and generation approach are sufficiently defined.
