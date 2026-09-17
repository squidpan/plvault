# Ultimate Requirements

An Obsidian-first laboratory for developing a reusable visual requirements-synthesis method.

## Delivery sequence

1. Reconstruct and study the Genesis one-page narrative.
2. Extract an independent visual grammar and metadata standard.
3. Apply the method to the Farm Credit proof of concept.
4. Refine it against the Fidelity Rep Code Expansion work.

## Working conventions

- Use lowercase kebab-case filenames.
- Keep Markdown and YAML as the authoritative semantic layer.
- Use Canvas for assembled navigation and relationships.
- Use Excalidraw for curated visual synthesis.
- Preserve source provenance in `references/bibleproject/sources.yaml`.
- Treat BibleProject material as private, noncommercial reference material.

## Obsidian

Open this repository as a vault or link it into an existing vault. The Genesis poster is stored by a unique filename, allowing Obsidian to resolve the Excalidraw wiki-link without a space-containing path.

## Git initialization

```bash
cd "$REPOS_ROOT/ultimate-requirements"
git init
git branch -m main
git switch -c feature/genesis-foundation
git add .
git status --short
git commit -m "Build Genesis requirements synthesis foundation"
```

Keep the remote repository private while it contains third-party reference files.
