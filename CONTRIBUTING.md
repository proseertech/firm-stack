# Contributing to firm-stack

Contributions from accounting professionals are welcome. If you have a workflow that would benefit others — a return review checklist, a close procedure, a planning analysis — please share it.

---

## How to Add a Skill

### 1. Pick a category

| Category | Naming Convention | Examples |
|---|---|---|
| Client communications | `<action>` | `client-email`, `tax-memo` |
| Tax return reviews | `<form>-review` | `1040-review`, `1120s-review` |
| CAS / close | `<workflow>` | `close`, `reconcile`, `fixed-assets` |
| Excel productivity | `excel-<action>` | `excel-formula-refresh`, `excel-report-format` |
| Tax planning analysis | `<strategy>-analysis` | `costseg-analysis`, `rd-analysis` |

All skills live as flat folders under `skills/`. No nesting.

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

```bash
claude --plugin-dir .
```

Then invoke your skill and verify it works with realistic (anonymized) data.

### 5. Open a pull request

- Target the `main` branch
- Include one skill per PR
- Describe what the skill does and what you tested it against

---

## Skill Quality Standards

- **Evidence-based** — every finding should point to a specific line item, account, or document. No vague observations.
- **Actionable** — the output should tell the user what to do next, not just what was found.
- **Control-aware** — accounting skills must treat control points seriously. A skill that bypasses human review of a material item is a defect.
- **Platform-agnostic** — core skills should work regardless of GL system. Integration skills use `<platform>-<action>` naming and live alongside core skills in `skills/`.
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
