# Firm Configuration Guide

How to configure firm-stack for your specific practice.

---

## Plugin Config (recommended)

When you install firm-stack as a plugin, you'll be prompted for these settings:

| Setting | Description | Example |
|---|---|---|
| `materiality_threshold` | Dollar amount below which Claude auto-corrects; above which it asks | `2500` |
| `gl_system` | Primary general ledger platform | `Sage Intacct` |
| `tax_software` | Tax preparation software | `Lacerte` |
| `fiscal_year_end` | Fiscal year-end | `December 31` |
| `capitalization_threshold` | Dollar threshold for capitalizing vs. expensing | `2500` |

These values are stored in your plugin config and available to all skills automatically. To update them later, use `/plugin config firm-stack`.

---

## Manual Configuration (fallback)

If you're not using the plugin install (e.g., using the git clone method or org-level skill upload), add this block to your **project's** `CLAUDE.md`:

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

Do **not** edit the firm-stack plugin's CLAUDE.md with your firm's settings — those changes would be overwritten on update.

### Options

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

Integration skills require API credentials stored in `.env` files (never committed to git). See the setup instructions for each platform:

- [Sage Intacct](../integrations/sage-intacct/README.md)
- [QuickBooks Online](../integrations/qbo/README.md)
- [Karbon](../integrations/karbon/README.md)

---

## If No Configuration Is Present

Skills will prompt the user for required context at runtime. Adding configuration reduces friction but is not required to use firm-stack.
