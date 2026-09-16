# Firm Configuration Guide

How to configure firm-stack for your specific practice.

---

## Plugin Config (recommended)

When you install firm-stack as a plugin, you'll be prompted for these settings:

| Setting | Description | Example |
|---|---|---|
| `materiality_threshold` | Dollar amount below which Claude auto-corrects; above which it asks | `2500` |
| `gl_system` | Primary general ledger platform | `Sage Intacct` |
| `tax_software` | Tax preparation software | `CCH Axcess` |
| `fiscal_year_end` | Fiscal year-end | `December 31` |
| `capitalization_threshold` | Dollar threshold for capitalizing vs. expensing | `2500` |

These values are stored in your plugin config. A skill picks one up only where
it explicitly references the variable — e.g. `${user_config.capitalization_threshold}`
in `fixed-assets`. Skills that do not reference a setting are not affected by it,
so a new skill must opt in by naming the variable in its `SKILL.md`. To update the
values later, use `/plugin config firm-stack`.

**Which settings are firm policy.** Only `materiality_threshold` and
`capitalization_threshold` are firm-configurable amounts. Statutory figures —
the FBAR $10,000 aggregate, the §195 $5,000/$50,000 start-up limits, the Form
1125-E $500,000 line, the gift tax annual exclusion — are set by law and must
never be driven from firm config.

---

## Manual Configuration (fallback)

If you're not using the plugin install (e.g., using the git clone method or org-level skill upload), add this block to your **project's** `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Materiality threshold: $2,500
- Fiscal year-end: December 31
- GL system: Sage Intacct
- Capitalization threshold: $2,500
- Tax software: CCH Axcess
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
| `Tax software` | Used by return review skills for format-specific guidance | `CCH Axcess` |
| `Return types` | Which tax return review skills are relevant to your practice | `1040, 1120S, 1065` |

---

## If No Configuration Is Present

Skills will prompt the user for required context at runtime. Adding configuration reduces friction but is not required to use firm-stack.
