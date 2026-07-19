---
id: PLAYBOOK-CS-001
project: career-system
type: operational-playbook
status: active

categories:
  - "[[Playbooks]]"
  - "[[Operations]]"

tags:
  - career-system
  - operations
  - job-acquisition
  - raw-jd
  - workflow

description: Acquire and prepare a Raw Job Description for Career System processing.

created: 2026-07-17
updated: 2026-07-17
---

# PLAYBOOK-CS-001
# Job Acquisition and Preparation

## Purpose

Acquire a Job Description from an external source and produce a validated
Raw Job Description suitable for downstream Career System processing.

This playbook documents the current operational workflow.

Engineering definitions for templates, schemas, identifiers, metadata, and
lifecycle management are maintained separately by the Engineering Knowledge
Framework.

---

## Scope

This playbook documents the following operational stages.

    Locate Job Posting
            ↓
    Capture Raw JD
            ↓
    Validate Raw JD
            ↓
    Handoff to JD Normalization

This playbook does not cover:

- JD Normalization
- Resume Asset Selection
- Resume Assembly
- Resume Enhancement
- ATS Resume Generation
- Application Package Generation
- Application Tracking

---

## Inputs

A publicly available Job Description from a supported source.

Current operational sources include:

- LinkedIn
- Teal
- Dice
- Employer career sites
- Other sources capable of producing a valid Raw JD Markdown document

LinkedIn is currently the preferred direct acquisition source.

Teal may be used as the source when a role has already been collected in the
Teal job tracker.

Dice currently requires a manual capture workflow when Web Clipper capture is
unavailable or incomplete.

---

## Input Artifact — Raw Job Description

The operational input to the Career System pipeline is a Raw Job Description
Markdown document.

A valid Raw JD contains:

- YAML frontmatter
- Complete Job Description body
- Source traceability information
- Capture metadata

The Raw JD is the authoritative source artifact for downstream processing.

The current operational YAML structure is:

    ---
    id:
    slug:
    type:
      - "jd"
    title:
    categories:
      - "[[Clippings]]"
      - "[[Careers]]"
      - "[[JDs]]"
    tags:
      - "clippings"
      - "career"
      - "jd"
      - "raw"
    status: "raw"
    version: "v1"
    capture_template_version: "v1"
    created: 2026-06-15
    last: 2026-06-15
    company:
    company_slug:
    source_system: "teal"
    source_file:
    source_url: "https://app.tealhq.com/job-tracker/ddb3fe61-50db-4575-a591-384d74650dcf"
    origin: "webclipper"
    run_id:
    captured_date: 2026-06-15
    source_title:
    normalized_title:
    role_id:
    role_family:
    role_level:
    role_qualifiers:
    role_code:
    role_code_confidence:
    role_summary:
    jd_file_name:
    jd_source_type: "clipped"
    jd_text_status: "raw"
    role_source_type: "jd"
    normalization_status: "pending"
    normalized_jd_id:
    ---

This YAML documents the current operational implementation.

The populated dates, source system, source URL, and other source-specific
values shown above are examples from an existing Raw JD. They must be replaced
with values belonging to the job posting being captured.

Detailed definitions, ownership, lifecycle rules, and future revisions are
maintained through EFK templates, schemas, examples, and standards.

---

## Current Capture Values

The current Obsidian Web Clipper workflow typically sets:

    type:
      - "jd"

    status: "raw"
    version: "v1"
    capture_template_version: "v1"
    origin: "webclipper"
    jd_source_type: "clipped"
    jd_text_status: "raw"
    role_source_type: "jd"
    normalization_status: "pending"

The following values depend on the posting being captured:

- `id`
- `slug`
- `title`
- `created`
- `last`
- `company`
- `company_slug`
- `source_system`
- `source_file`
- `source_url`
- `captured_date`
- `source_title`
- `jd_file_name`

The following values may remain empty during initial acquisition and may be
populated by downstream processing:

- `run_id`
- `normalized_title`
- `role_id`
- `role_family`
- `role_level`
- `role_qualifiers`
- `role_code`
- `role_code_confidence`
- `role_summary`
- `normalized_jd_id`

---

## Deliverable

A validated Raw JD Markdown document.

Example:

    jd-raw-lseg-business-analyst-20260717.md

---

## Prerequisites

- Career System repository
- Current approved Raw JD capture template
- Obsidian Web Clipper for the preferred capture workflow
- Access to the target Job Description
- Permission to save the captured document in the appropriate Career System
  data location

---

## Stage 1 — Locate Job Posting

### Objective

Identify the Job Description that will enter the Career System pipeline.

### Inputs

- Job search criteria
- Target employer or recruiter
- Supported job board or employer career site

### Procedure

1. Locate the target job posting.
2. Review the posting for relevance.
3. Confirm that the employer and job title are visible.
4. Confirm that the complete Job Description is accessible.
5. Record or preserve the source URL.
6. Confirm that the posting has not already been captured.

### Success Criteria

- Correct job posting identified.
- Employer and job title visible.
- Source URL available.
- Complete Job Description accessible.
- Posting ready for capture.

### Output

Selected Job Description.

---

## Stage 2 — Capture Raw Job Description

### Objective

Capture the Job Description as a Raw JD Markdown document.

### Inputs

- Selected Job Description
- Current approved Raw JD template

### Preferred Workflow

Use the approved Obsidian Web Clipper template.

Template location:

    data/templates/jd/raw/jd-raw-webclipper-template.json

The Web Clipper should create a Markdown document containing:

- Raw JD YAML frontmatter
- Complete Job Description body
- Source URL
- Capture date
- Source-specific metadata

The resulting Markdown document becomes the operational pipeline input
artifact.

### Manual Workflow

Use the manual workflow when:

- Web Clipper cannot access the posting.
- The clipped content is incomplete.
- The source page structure prevents a valid capture.
- The posting originates from a source not supported by the current template.

Procedure:

1. Copy a previously validated Raw JD document.
2. Replace the complete Job Description body.
3. Replace all job-specific YAML values.
4. Remove identifiers and values belonging to the copied document.
5. Set the correct source URL and source system.
6. Set `origin` and `jd_source_type` to values representing the actual capture
   method.
7. Save the document using the current Raw JD naming convention.

Dice postings are a current example of the manual workflow.

### Success Criteria

- Raw JD Markdown document created.
- YAML frontmatter present.
- Complete Job Description captured.
- Source URL preserved.
- Source-specific values updated.

### Output

Raw JD Markdown document.

---

## Stage 3 — Validate Raw Job Description

### Objective

Verify that the Raw JD satisfies the current operational input contract.

### Inputs

- Raw JD Markdown document

### Metadata Validation

Confirm:

- YAML frontmatter begins and ends with `---`.
- `type` includes `jd`.
- `status` is `raw`.
- `version` is present.
- `company` identifies the employer.
- `source_title` or `title` preserves the original job title.
- `source_system` identifies the capture source.
- `source_url` identifies the source posting.
- `captured_date` is present.
- `jd_text_status` is `raw`.
- `role_source_type` is `jd`.
- `normalization_status` is `pending`.

### Content Validation

Confirm:

- Job Description body is present.
- Job Description is complete.
- Responsibilities are included.
- Qualifications are included when present in the source.
- Employer and role information match the source posting.
- Navigation menus are removed.
- Recommended-job content is removed.
- Advertising and unrelated page content are removed.
- No content from a different posting remains in the document.

### File Validation

Confirm:

- Document uses the `.md` extension.
- File name follows the current Raw JD naming convention.
- File is saved in the expected Career System data location.
- File can be opened as Markdown.
- YAML frontmatter remains parseable.

### Validation Result

If validation succeeds:

- Accept the Raw JD.
- Proceed to JD Normalization.

If validation fails:

- Correct the identified deficiencies.
- Repeat Raw JD validation.
- Do not proceed to normalization until the document passes validation.

### Success Criteria

Validated Raw JD ready for normalization.

### Output

Validated Raw JD Markdown document.

---

## Exception Handling

### Source Posting Is No Longer Available

- Preserve any previously captured source content.
- Record that the source is no longer accessible.
- Do not reconstruct missing Job Description content from memory.
- Use an alternate authoritative source only when the same posting can be
  verified.

### Web Clipper Produces Incomplete Content

- Do not accept the incomplete clip.
- Retry the capture.
- Use the manual workflow when retrying does not produce a complete document.

### Required Source Metadata Is Missing

- Populate the value from the source posting when available.
- Leave downstream-derived fields empty.
- Do not invent identifiers, classifications, or normalized values.

### Copied Raw JD Contains Previous-Role Data

- Remove all values belonging to the previous role.
- Recheck the entire YAML section.
- Recheck the document body.
- Repeat validation before normalization.

---

## Exit Criteria

This playbook is complete when:

- Job posting has been identified.
- Raw JD has been captured.
- Raw JD YAML has been validated.
- Raw JD content has been validated.
- Raw JD has been stored in the expected location.
- Raw JD is ready for [[PLAYBOOK-CS-002 JD Normalization]].

---

## Operational Decisions

| Decision | Current Implementation |
|---|---|
| Canonical pipeline input | Raw JD Markdown |
| Canonical document structure | YAML frontmatter and Markdown body |
| Preferred direct source | LinkedIn |
| Existing tracker source | Teal |
| Preferred capture tool | Obsidian Web Clipper |
| Alternate capture method | Manual capture |
| Engineering artifact ownership | EFK |
| Operational workflow ownership | Operations |

---

## Related Artifacts

### Templates

    data/templates/jd/raw/jd-raw-webclipper-template.json

### Template Documentation

    data/templates/jd/raw/README.md

### Related Playbooks

- [[PLAYBOOK-CS-002 JD Normalization]]

### Related Requirements

- [[EPIC-CS-003]]

---

## Version History

| Version | Date | Description |
|---|---|---|
| v0.1 | 2026-07-17 | Initial operational playbook for Job Acquisition and Preparation. |
| v0.2 | 2026-07-17 | Added Raw JD input contract, detailed validation, manual capture workflow, and exception handling. |
