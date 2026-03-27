# Firm Configuration Guide

How to configure firm-stack for your specific practice.

---

## Where Configuration Lives

firm-stack reads configuration from the `firm-stack Configuration` block in your **project's** `CLAUDE.md` file. This keeps your firm-specific settings separate from the shared skill definitions.

Do **not** edit `~/.claude/skills/firm-stack/CLAUDE.md` with your firm's settings — those changes would be overwritten on the next `git pull`.

---

## Configuration Block

Add this to your project's `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Materiality threshold: $2,500
- Fiscal year-end: December 31
- GL system: Sage Intacct
- Capitalization threshold: $2,500
- Active integrations: sage-intacct, qbo, karbon
- Tax software: Lacerte
- Return types: 1040, 1120S, 1065, 1041, 990PF
```

---

## Options

| Key | Description | Example |
|---|---|---|
| `Materiality threshold` | Dollar amount below which Claude auto-corrects; above which it asks | `$2,500` |
| `Fiscal year-end` | Used by close and reporting skills | `December 31` |
| `GL system` | Primary general ledger platform | `Sage Intacct` |
| `Capitalization threshold` | For fixed asset skills — R&M vs. capitalize | `$2,500` |
| `Active integrations` | Which integration modules to enable | `sage-intacct, qbo, karbon` |
| `Tax software` | Used by return review skills for format-specific guidance | `Lacerte` |
| `Return types` | Which tax return review skills are relevant to your practice | `1040, 1120S, 1065` |

---

## Integration Setup

Each integration requires additional setup (API credentials, etc.). See the README in each integration directory:

- [integrations/sage-intacct/README.md](../integrations/sage-intacct/README.md)
- [integrations/qbo/README.md](../integrations/qbo/README.md)
- [integrations/karbon/README.md](../integrations/karbon/README.md)

---

## If No Configuration Is Present

Skills will prompt the user for required context at runtime. Adding a configuration block reduces friction but is not required to use firm-stack.
