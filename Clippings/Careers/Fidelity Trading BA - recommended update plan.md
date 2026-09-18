---
categories:
  - "[[Clippings]]"
title: Fidelity Trading BA - recommended plan
source: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a99b743-afec-83ea-b444-3db7a07cf29b
author:
published:
created: 2026-09-16
description: Fidelity Trading BA - recommended plan
tags:
  - clippings
url: https://chatgpt.com/g/g-p-69dd57df00d0819198410a853ec753d1/c/6a99b743-afec-83ea-b444-3db7a07cf29b
---
Worked for 9s

The repository upgrade is committed successfully and your working tree is clean. One cleanup remains: you committed the trailing-whitespace warnings reported by `git diff --cached --check`.

They aren’t functional errors, but we should fix them now and amend the commit.

Run:

```markdown
cd ~/pjs/repos/fidelity-rep-code-ba-prep

sed -i 's/[[:space:]]\+$//' \
  archive/docs/SQL-REFRESHER-V1.md \
  docs/requirements/AC-RCE-101.md

git diff --check
python3 scripts/validate_artifacts.py
git diff
```

Then amend the existing commit:

```markdown
git add \
  archive/docs/SQL-REFRESHER-V1.md \
  docs/requirements/AC-RCE-101.md

git commit --amend --no-edit
```

Final confirmation:

```markdown
git status
git diff --check
git log -1 --oneline
```

Expected:

- `git status`: working tree clean
- `git diff --check`: no output
- Validator: `Validation PASS`

One small formatting caveat: the trailing spaces in `AC-RCE-101.md` were being used as Markdown forced line breaks between Given/When/Then. Removing them won’t change the requirements’ meaning, but some Markdown viewers may display each trio as one paragraph. That is acceptable for now; when we review the artifact, we can convert each scenario to a cleaner table or properly spaced Given/When/Then structure.

After this cleanup, the repository is ready. Our next working session should begin with:

```markdown
less docs/requirements/00-RCE-WALKTHROUGH.md
```

Then we’ll walk the chain as a BA would during a Development handoff and evaluate whether each artifact actually provides enough context to build and test the change.

\[PL\] pl@pop-os:~/pjs/repos/fidelity-rep-code-ba-prep $ cd ~/pjs/repos/fidelity-rep-code-ba-prep sed -i 's/\[\[:space:\]\]\\+$//' \\ archive/docs/SQL-REFRESHER-V1.md \\ docs/requirements/AC-RCE-101.md git diff --check python3 scripts/validate\_artifacts.py git diff Markdown files: 24; front-matter artifacts: 14 Validation PASS: YAML, IDs, classifications, types, and local wiki links are valid. diff --git a/archive/docs/SQL-REFRESHER-V1.md b/archive/docs/SQL-REFRESHER-V1.md index 5cf7255..159d513 100644 --- a/archive/docs/SQL-REFRESHER-V1.md +++ b/archive/docs/SQL-REFRESHER-V1.md @@ -1,7 +1,7 @@ # Session 8 — PostgreSQL Refresher -Suggested database: `synthetic_rep_code_ba_lab` -Schema: `repcode_lab` +Suggested database: `synthetic_rep_code_ba_lab` +Schema: `repcode_lab` PostgreSQL: 14.23 ## Purpose diff --git a/docs/requirements/AC-RCE-101.md b/docs/requirements/AC-RCE-101.md index 4f19547..0eb0d6a 100644 --- a/docs/requirements/AC-RCE-101.md +++ b/docs/requirements/AC-RCE-101.md @@ -22,39 +22,39 @@ related: \["\[\[BR-RCE-001\]\]", "\[\[INT-RCE-001\]\]"\] ## AC-RCE-101-01 — Active unique mapping -\*\*Given\*\* expanded identifier `A7Q4`, legacy consumer `LEGACY-ROUTER-1`, and one active mapping to `K42` -\*\*When\*\* the transaction is prepared for that consumer -\*\*Then\*\* the outbound legacy field contains `K42` +\*\*Given\*\* expanded identifier `A7Q4`, legacy consumer `LEGACY-ROUTER-1`, and one active mapping to `K42` +\*\*When\*\* the transaction is prepared for that consumer +\*\*Then\*\* the outbound legacy field contains `K42` \*\*And\*\* the authoritative transaction retains `A7Q4`. ## AC-RCE-101-02 — No active mapping -\*\*Given\*\* a valid expanded identifier with no active mapping for the processing time -\*\*When\*\* translation is requested -\*\*Then\*\* no legacy message is sent +\*\*Given\*\* a valid expanded identifier with no active mapping for the processing time +\*\*When\*\* translation is requested +\*\*Then\*\* no legacy message is sent \*\*And\*\* the transaction enters a controlled exception state with reason `NO_ACTIVE_MAPPING`. ## AC-RCE-101-03 — Multiple active mappings -\*\*Given\*\* more than one active candidate mapping for the same expanded identifier and consumer -\*\*When\*\* translation is requested -\*\*Then\*\* no alias is selected +\*\*Given\*\* more than one active candidate mapping for the same expanded identifier and consumer +\*\*When\*\* translation is requested +\*\*Then\*\* no alias is selected \*\*And\*\* the transaction enters exception state `AMBIGUOUS_MAPPING`. ## AC-RCE-101-04 — Expired mapping -\*\*Given\*\* a mapping whose effective end precedes the transaction's processing time -\*\*When\*\* translation is requested +\*\*Given\*\* a mapping whose effective end precedes the transaction's processing time +\*\*When\*\* translation is requested \*\*Then\*\* the expired mapping is not used. ## AC-RCE-101-05 — Audit evidence -\*\*Given\*\* any translation attempt -\*\*When\*\* processing completes or stops +\*\*Given\*\* any translation attempt +\*\*When\*\* processing completes or stops \*\*Then\*\* audit evidence records the input, selected output if any, mapping version, consumer, timestamp, outcome/reason, and correlation ID without exposing prohibited sensitive data. ## AC-RCE-101-06 — Retry consistency -\*\*Given\*\* a retry with the same correlation ID and unchanged effective mapping version -\*\*When\*\* translation is repeated +\*\*Given\*\* a retry with the same correlation ID and unchanged effective mapping version...skipping... --- a/archive/docs/SQL-REFRESHER-V1.md +++ b/archive/docs/SQL-REFRESHER-V1.md @@ -1,7 +1,7 @@ # Session 8 — PostgreSQL Refresher -Suggested database: `synthetic_rep_code_ba_lab` -Schema: `repcode_lab` +Suggested database: `synthetic_rep_code_ba_lab` +Schema: `repcode_lab` PostgreSQL: 14.23 ## Purpose diff --git a/docs/requirements/AC-RCE-101.md b/docs/requirements/AC-RCE-101.md index 4f19547..0eb0d6a 100644 --- a/docs/requirements/AC-RCE-101.md +++ b/docs/requirements/AC-RCE-101.md @@ -22,39 +22,39 @@ related: \["\[\[BR-RCE-001\]\]", "\[\[INT-RCE-001\]\]"\] ## AC-RCE-101-01 — Active unique mapping -\*\*Given\*\* expanded identifier `A7Q4`, legacy consumer `LEGACY-ROUTER-1`, and one active mapping to `K42` -\*\*When\*\* the transaction is prepared for that consumer -\*\*Then\*\* the outbound legacy field contains `K42` +\*\*Given\*\* expanded identifier `A7Q4`, legacy consumer `LEGACY-ROUTER-1`, and one active mapping to `K42` +\*\*When\*\* the transaction is prepared for that consumer +\*\*Then\*\* the outbound legacy field contains `K42` \*\*And\*\* the authoritative transaction retains `A7Q4`. ## AC-RCE-101-02 — No active mapping -\*\*Given\*\* a valid expanded identifier with no active mapping for the processing time -\*\*When\*\* translation is requested -\*\*Then\*\* no legacy message is sent +\*\*Given\*\* a valid expanded identifier with no active mapping for the processing time +\*\*When\*\* translation is requested +\*\*Then\*\* no legacy message is sent \*\*And\*\* the transaction enters a controlled exception state with reason `NO_ACTIVE_MAPPING`. ## AC-RCE-101-03 — Multiple active mappings -\*\*Given\*\* more than one active candidate mapping for the same expanded identifier and consumer -\*\*When\*\* translation is requested -\*\*Then\*\* no alias is selected +\*\*Given\*\* more than one active candidate mapping for the same expanded identifier and consumer +\*\*When\*\* translation is requested +\*\*Then\*\* no alias is selected \*\*And\*\* the transaction enters exception state `AMBIGUOUS_MAPPING`. ## AC-RCE-101-04 — Expired mapping -\*\*Given\*\* a mapping whose effective end precedes the transaction's processing time -\*\*When\*\* translation is requested +\*\*Given\*\* a mapping whose effective end precedes the transaction's processing time +\*\*When\*\* translation is requested \*\*Then\*\* the expired mapping is not used. ## AC-RCE-101-05 — Audit evidence -\*\*Given\*\* any translation attempt -\*\*When\*\* processing completes or stops +\*\*Given\*\* any translation attempt +\*\*When\*\* processing completes or stops \*\*Then\*\* audit evidence records the input, selected output if any, mapping version, consumer, timestamp, outcome/reason, and correlation ID without exposing prohibited sensitive data. ## AC-RCE-101-06 — Retry consistency -\*\*Given\*\* a retry with the same correlation ID and unchanged effective mapping version -\*\*When\*\* translation is repeated +\*\*Given\*\* a retry with the same correlation ID and unchanged effective mapping version +\*\*When\*\* translation is repeated \*\*Then\*\* the same outcome is returned without creating a duplicate downstream delivery. \[PL\] pl@pop-os:~/pjs/repos/fidelity-rep-code-ba-prep $ git add \\ archive/docs/SQL-REFRESHER-V1.md \\ docs/requirements/AC-RCE-101.md git commit --amend --no-edit \[refactor/synthetic-ba-lab 6d5add5\] Evolve prep repo into synthetic BA requirements case study Date: Wed Sep 16 14:12:35 2026 -0400 40 files changed, 1146 insertions(+), 264 deletions(-) create mode 100644.gitignore rewrite README.md (99%) rename diagrams/TRD-21-rep-code-translation-legacy-compatibility-v2.puml => archive/diagrams/TRD-21-rep-code-translation-legacy-compatibility.puml (69%) rename docs/domain/SESSION-8-SQL-REFRESHER.md => archive/docs/SQL-REFRESHER-V1.md (95%) rename sql/fidelity-rep-code-sql-lab.sql => archive/sql/rep-code-sql-lab-v1.sql (95%) create mode 100644 diagrams/repcode\_ERD.puml create mode 100644 docs/REVIEW-AND-REVISION-NOTES.md rename docs/domain/{SESSION-SUMMARY-1-6.md => DOMAIN-FOUNDATIONS.md} (93%) create mode 100644 docs/domain/SQL-ANALYSIS-GUIDE.md delete mode 100644 docs/interview/.gitkeep create mode 100644 docs/requirements/00-RCE-WALKTHROUGH.md create mode 100644 docs/requirements/AC-RCE-101.md create mode 100644 docs/requirements/BR-RCE-001.md create mode 100644 docs/requirements/DATA-RCE-001.md create mode 100644 docs/requirements/DEC-RCE-001.md create mode 100644 docs/requirements/DISC-RCE-001.md create mode 100644 docs/requirements/EPIC-RCE-001.md create mode 100644 docs/requirements/FEATURE-RCE-010.md create mode 100644 docs/requirements/INT-RCE-001.md create mode 100644 docs/requirements/LINEAGE-RCE-001.md create mode 100644 docs/requirements/MAP-RCE-001.md create mode 100644 docs/requirements/RISK-RCE-001.md create mode 100644 docs/requirements/RTM-RCE-001.csv create mode 100644 docs/requirements/TC-RCE-101-01.md create mode 100644 docs/requirements/TC-RCE-101-02.md create mode 100644 docs/requirements/US-RCE-101.md delete mode 100644 docs/status/PROJECT-STATUS-2026-08-22.md delete mode 100644 docs/status/PROJECT-STATUS-2026-08-23.md delete mode 100644 docs/status/PROJECT-STATUS-2026-08-24.md delete mode 100644 exercises/.gitkeep create mode 100644 exercises/DISCOVERY-EXERCISE.md create mode 100644 requirements-dev.txt create mode 100644 scripts/validate\_artifacts.py delete mode 100644 sources/.gitkeep create mode 100644 sources/SOURCE-BOUNDARY.md rewrite sql/README.md (86%) create mode 100644 sql/synthetic-rep-code-ba-lab.sql \[PL\] pl@pop-os:~/pjs/repos/fidelity-rep-code-ba-prep $ git status git diff --check git log -1 --oneline On branch refactor/synthetic-ba-lab nothing to commit, working tree clean 6d5add5 (HEAD -> refactor/synthetic-ba-lab) Evolve prep repo into synthetic BA requirements case study \[PL\] pl@pop-os:~/pjs/repos/fidelity-rep-code-ba-prep $

Perfect. The repository is clean, validated, and committed on:

```markdown
refactor/synthetic-ba-lab
```

Latest commit:

```markdown
6d5add5 Evolve prep repo into synthetic BA requirements case study
```

The earlier commit `c7ca088` was correctly replaced by the amended commit, so use `6d5add5` if you need to reference this checkpoint.

Next time, we’ll begin the practical BA review with:

```markdown
less docs/requirements/00-RCE-WALKTHROUGH.md
```

Then follow the chain:

```markdown
Discovery
  → Epic
  → Feature
  → Story
  → Acceptance Criteria
  → Rules / Data / Interface / Decision / Risk
  → Lineage and Mapping
  → Test Cases
  → RTM
  → Development handoff
```

We’ll review it as though you are preparing for refinement and handing the work to Development and QA—not merely checking whether the documents exist.

Today 3:14 PM

I want to be able to look at these from Obsidian. This is from Requirements Layout Design chat: copy over the files to plvault this way:  
You’re right: if **`plvault`** **must remain standalone**, copying is better than a symbolic link.

A symlink would create two issues:

- The `plvault` Git repository would normally track only the symlink—not the linked files.
- A clone or backup of `plvault` on another computer would contain a broken link unless the separate repository existed at exactly the same path.

The symlink is convenient, but it conflicts with your standalone-vault requirement.

## Recommended model

Use the workflow you have already been following:

- **Obsidian vault = authoring/master workspace**
- **`ultimate-requirements`** **repository = controlled project snapshot**
- Copy changes between them deliberately.
- Never edit both copies independently during the same work session.

For now, copy the repository content into the vault—excluding its `.git` directory.

First check the intended destination:

```bash
ls -ld \
  "$VAULTS_ROOT/plvault/References/ultimate-requirements"
```

If it does not exist, copy the project:

```bash
mkdir -p \
  "$VAULTS_ROOT/plvault/References/ultimate-requirements"

rsync -av \
  --exclude='.git/' \
  "$REPOS_ROOT/ultimate-requirements/" \
  "$VAULTS_ROOT/plvault/References/ultimate-requirements/"
```

Verify that it is a real directory, not a link:

```bash
test -d "$VAULTS_ROOT/plvault/References/ultimate-requirements" \
  && test ! -L "$VAULTS_ROOT/plvault/References/ultimate-requirements" \
  && echo "Standalone vault copy confirmed"
```

Open the skeleton:

```bash
xdg-open \
  'obsidian://open?vault=plvault&file=References/ultimate-requirements/examples/genesis/excalidraw/genesis-layout-skeleton-v0.1.excalidraw.md'
```

## After editing in Obsidian

Because the vault is the authoring master, copy its changes back into the project repository before committing:

```bash
rsync -av \
  --exclude='.git/' \
  "$VAULTS_ROOT/plvault/References/ultimate-requirements/" \
  "$REPOS_ROOT/ultimate-requirements/"

cd "$REPOS_ROOT/ultimate-requirements"

git status --short
git diff --check
git diff
```

This gives you:

- A fully self-contained `plvault`
- Immediate Obsidian access
- A clean, dedicated project repository
- Deliberate review before anything is committed

Later we should turn those `rsync` commands into two clearly named scripts, such as:

```markdown
scripts/copy-repo-to-vault.sh
scripts/copy-vault-to-repo.sh
```

That will reduce path mistakes and make the direction of each copy unmistakable.

Worked for 24s

Yes—we should use the same standalone-copy approach for this repository. That lets Obsidian display and edit the Markdown artifacts while Git remains the controlled project history.

Use this destination name so the vault reflects the repository’s new purpose:

```markdown
plvault/References/synthetic-rep-code-ba-lab
```

### 1\. Confirm variables and source

```markdown
printf 'REPOS_ROOT=%s\nVAULTS_ROOT=%s\n' \
  "$REPOS_ROOT" \
  "$VAULTS_ROOT"

cd "$REPOS_ROOT/fidelity-rep-code-ba-prep"

git branch --show-current
git status --short
```

You should see:

```markdown
refactor/synthetic-ba-lab
```

with no status output.

### 2\. Create the standalone vault copy

```markdown
mkdir -p \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab"

rsync -av \
  --exclude='.git/' \
  "$REPOS_ROOT/fidelity-rep-code-ba-prep/" \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab/"
```

Confirm that it is a real directory:

```markdown
test -d \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab" \
  && test ! -L \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab" \
  && echo "Standalone vault copy confirmed"
```

### 3\. Open the requirements walkthrough

```markdown
xdg-open \
  'obsidian://open?vault=plvault&file=References/synthetic-rep-code-ba-lab/docs/requirements/00-RCE-WALKTHROUGH.md'
```

You can also open the repository root in the file manager:

```markdown
xdg-open \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab"
```

### 4\. What you should see in Obsidian

Start with:

```markdown
00-RCE-WALKTHROUGH
```

Its links should let you navigate through:

```markdown
EPIC-RCE-001
FEATURE-RCE-010
US-RCE-101
AC-RCE-101
BR-RCE-001
DATA-RCE-001
INT-RCE-001
DEC-RCE-001
RISK-RCE-001
LINEAGE-RCE-001
MAP-RCE-001
TC-RCE-101-01
TC-RCE-101-02
```

The YAML front matter should also make these artifacts usable later with Obsidian Bases.

PlantUML `.puml` files will be readable as text. Rendering them inside Obsidian will require a PlantUML-compatible community plugin or exported PNG/SVG versions. We can address that separately.

### After editing in Obsidian

Treat the vault copy as your authoring workspace. Before copying anything back, preview the synchronization:

```markdown
rsync -av --dry-run \
  --exclude='.git/' \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab/" \
  "$REPOS_ROOT/fidelity-rep-code-ba-prep/"
```

If the preview is correct:

```markdown
rsync -av \
  --exclude='.git/' \
  "$VAULTS_ROOT/plvault/References/synthetic-rep-code-ba-lab/" \
  "$REPOS_ROOT/fidelity-rep-code-ba-prep/"
```

Then review through Git:

```markdown
cd "$REPOS_ROOT/fidelity-rep-code-ba-prep"

git status --short
git diff --check
python3 scripts/validate_artifacts.py
git diff
```

Do not use `--delete` when copying from the vault back to the repository until we create guarded synchronization scripts. A mistaken direction with `--delete` could remove repository files.

The next useful improvement is indeed two directional scripts with dry-run as the default:

```markdown
scripts/copy-repo-to-vault.sh
scripts/copy-vault-to-repo.sh
```

That will make the authoritative direction explicit and substantially reduce sync mistakes.