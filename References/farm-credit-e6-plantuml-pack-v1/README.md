# Farm Credit Debt Platform Interview Prep — E6 PlantUML Pack v1

## Scope

Epic E6 — Issue and Settle Security.

This pack starts with pictures and keeps the diagrams traceable to the user story and acceptance criteria.
It is an interview-preparation model based on public Farm Credit and Fedwire concepts, not a claim about the Funding Corporation's proprietary target architecture.

## Files

1. `E6-00-core-users-and-data-exchange.puml` — context view of actors, systems, and information flows.
2. `E6-01-use-cases.puml` — actors and use cases for issuance and settlement.
3. `E6-02-sequence-happy-path.puml` — approved security through successful settlement and reconciliation.
4. `E6-03-sequence-exception-and-retry.puml` — rejected instruction, correction, resubmission, and escalation.
5. `E6-04-story-acceptance-criteria.md` — story, actors, data, ACs, and diagram traceability.

## Suggested study order

1. Read the context diagram.
2. Review the use-case diagram.
3. Walk through the happy-path sequence aloud.
4. Explain the exception-and-retry path.
5. Use the traceability table to connect each acceptance criterion to a diagram step.

## Rendering

```bash
plantuml E6-*.puml
```

Or render the files through your existing VS Code, IntelliJ, or Obsidian PlantUML workflow.
