# Raw JD Templates

## Purpose

This folder contains reusable input templates for Raw Job Description
documents used by Career System.

## Current Files

### `jd-raw-webclipper-template.json`

Importable Obsidian Web Clipper template for capturing LinkedIn Job
Descriptions as Markdown.

The Career System operational pipeline currently accepts Raw JD input as
Markdown (`.md`) only. It does not directly accept PDF, Word, plain-text, or
HTML input.

## Version Fields

- `schemaVersion` is the Obsidian Web Clipper JSON export format version.
- `capture_template_version` identifies the Career System capture template.
- `version` identifies the version of the individual Raw JD document produced
  from the template. It is not the Career System software version.

## Source Conventions

For a LinkedIn JD:

    source_system: "linkedin"
    origin: "webclipper"
    jd_source_type: "clipped"

For a Dice JD prepared manually from a previously validated Raw JD:

    source_system: "dice"
    origin: "manual"
    jd_source_type: "manual"

The manually prepared file must remain Markdown and retain the required Raw JD
YAML properties described in
[[PLAYBOOK-CS-001 Job Acquisition and Preparation]].
