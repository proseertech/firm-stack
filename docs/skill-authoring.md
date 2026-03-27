# Skill Authoring Guide

How to write a firm-stack skill that is clear, actionable, and safe to use in production.

---

## The Core Standard: Evidence-Based and Actionable

Every finding a skill surfaces must:
1. **Point to something specific** — an account, a line item, a document, a dollar amount. Not "revenue looks off" but "Line 1a gross receipts ($847,230) doesn't match the W-2 wages reported on Schedule D ($832,450) — $14,780 variance."
2. **Tell the user what to do next** — not just what was found, but what the recommended action is.

---

## SKILL.md Structure

```yaml
---
name: skill-slug          # lowercase, hyphenated — must match folder name
version: 1.0.0            # semantic versioning
description: |            # shown in skill registry
  ...
trigger: |                # phrases that auto-invoke the skill
  ...
allowed-tools:            # only include what the skill actually needs
  - Read
  - AskUserQuestion
tier: all-staff           # all-staff | power-user | developer
---
```

### Sections

| Section | Required | Purpose |
|---|---|---|
| Purpose | Yes | One paragraph: what problem, when to use |
| Required Inputs | Yes | What Claude needs before starting |
| Workflow | Yes | Numbered phases with validation gates |
| Control Points | Yes | Hard stops requiring human confirmation |
| Red Flags | Yes | Conditions that pause and surface to user |
| Output Format | Yes | What Claude delivers |
| Safety Constraints | Yes | What the skill must NOT do |

---

## Skill Naming

All skills live as flat folders under `skills/`. No nesting.

| Category | Convention | Examples |
|---|---|---|
| Core skills | `<descriptive-name>` | `close`, `reconcile`, `tax-memo` |
| Excel skills | `excel-<action>` | `excel-formula-refresh` |
| Planning skills | `<strategy>-analysis` | `costseg-analysis`, `rd-analysis` |
| Integration skills | `<platform>-<action>` | `intacct-import-je`, `qbo-pull-reports` |

The `name:` field in frontmatter must match the folder name exactly.

---

## Workflow Design

Structure workflows as sequential phases, not a flat list of steps. Each phase should have:
- A clear name
- What Claude does in the phase
- What it produces
- What the validation gate is before proceeding

**Good:**
> 1. **Gather source documents** — Ask the user to provide W-2s, 1099s, and brokerage statements for the tax year. Do not proceed until all required documents are confirmed present.

**Bad:**
> 1. Get the documents and check them.

---

## Control Points

A control point is a place where Claude must stop and wait for a human decision before proceeding. Use them for:
- Material findings (above the firm's materiality threshold)
- Anything that would result in a posted entry, filed document, or sent communication
- Situations where the user needs to exercise professional judgment

Control points are not optional. A skill that bypasses a material control point is a defect.

---

## Tiering

| Tier | When to use |
|---|---|
| `all-staff` | Skill requires only basic accounting knowledge, no judgment about materiality, no complex tax law |
| `power-user` | Skill involves judgment calls, materiality decisions, or knowledge of specific tax rules |
| `developer` | Skill requires API credentials, environment variables, or technical setup beyond Claude Code |

---

## Platform-Agnostic vs. Integration Skills

- **Core skills** should work regardless of which GL, tax software, or practice management system the firm uses. Refer to data by concept ("the trial balance", "the bank statement") not by system ("the Intacct export").
- **Integration skills** use `<platform>-<action>` naming (e.g., `intacct-import-je`, `qbo-pull-reports`) and may call specific APIs and assume specific data formats. They live alongside core skills in `skills/`.

---

## Testing Your Skill

Before submitting:
1. From the firm-stack repo root: `claude --plugin-dir .`
2. Invoke your skill with `/firm-stack:<your-skill-name>`
3. Run it with realistic (anonymized) data
4. Verify all control points trigger correctly
5. Verify red flags surface when expected
6. Confirm the output format matches what the skill describes
