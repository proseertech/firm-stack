# Contributing to firm-stack

Contributions from accounting professionals are welcome. If you have a workflow that would benefit others — a return review checklist, a close procedure, a planning analysis — please share it.

---

## How to Add a Skill

### 1. Pick a category

| Category | Directory | For |
|---|---|---|
| Client communications | `skills/` | Email, memos, client-facing output |
| Tax return reviews | `skills/` | Cross-referencing returns against source docs |
| CAS / close | `skills/` | Month-end workflows, JEs, reconciliations |
| Excel | `skills/excel/` | Excel formula and formatting skills |
| Tax planning analysis | `skills/planning/` | "Should we pursue this strategy?" screenings |
| Platform integrations | `integrations/<platform>/skills/` | Skills that call a specific GL or practice management API |

### 2. Copy the template

```bash
cp templates/SKILL.md.tmpl skills/<your-skill-name>/SKILL.md
```

### 3. Fill in the template

Every skill needs:
- **Frontmatter** — name, version, description, trigger phrases, allowed-tools, tier
- **Purpose** — one paragraph: what problem this solves and when to use it
- **Required Inputs** — what Claude needs before starting
- **Workflow** — numbered phases with validation gates
- **Control Points** — hard stops requiring human confirmation
- **Red Flags** — conditions that should pause the skill and surface to the user
- **Output Format** — what Claude produces
- **Safety Constraints** — what this skill must NOT do

See [docs/skill-authoring.md](docs/skill-authoring.md) for detailed guidance and examples.

### 4. Test it

Install firm-stack locally and run your skill in a real Claude Code session before submitting.

### 5. Open a pull request

- Target the `main` branch
- Include one skill per PR
- Describe what the skill does and what you tested it against

---

## Skill Quality Standards

- **Evidence-based** — every finding should point to a specific line item, account, or document. No vague observations.
- **Actionable** — the output should tell the user what to do next, not just what was found.
- **Control-aware** — accounting skills must treat control points seriously. A skill that bypasses human review of a material item is a defect.
- **Platform-agnostic** — core skills should work regardless of GL system. If a skill requires a specific platform, it belongs in `integrations/`.
- **No telemetry** — skills must not transmit data externally.

---

## Tiers

| Tier | Who it's for |
|---|---|
| `all-staff` | Any team member with basic accounting knowledge |
| `power-user` | Staff comfortable with more complex workflows and judgment calls |
| `developer` | Requires technical setup (API credentials, environment variables, etc.) |

---

## Questions

Open a [GitHub Discussion](https://github.com/larryb821/firm-stack/discussions) for questions, skill proposals, or feedback.
