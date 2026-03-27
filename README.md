# firm-stack

**Claude Code skills for accounting firms.**

A collection of slash-command skills that extend Claude Code with accounting-specific workflows — tax return review, month-end close, reconciliation, client communications, and more. Built by [Proseer](https://proseer.co), designed for any CPA or accounting firm.

Inspired by [gstack](https://github.com/garrytan/gstack) and [superpowers](https://github.com/obra/superpowers).

---

## Install

```bash
git clone https://github.com/larryb821/firm-stack ~/.claude/skills/firm-stack
```

Then add a `firm-stack` configuration block to your project's `CLAUDE.md` (see [docs/firm-config.md](docs/firm-config.md)).

---

## Skills

### Client Communications
| Skill | Purpose |
|---|---|
| `/client-email` | Polish CPA-to-client email drafts |
| `/tax-memo` | Draft client-facing tax memos from position notes |

### Tax Return Reviews
| Skill | Purpose |
|---|---|
| `/1040-review` | Form 1040 — individual return cross-reference |
| `/1120s-review` | Form 1120-S — S-corp return cross-reference |
| `/1120-review` | Form 1120 — C-corp return cross-reference |
| `/1065-review` | Form 1065 — partnership return cross-reference |
| `/990-review` | Form 990-PF — private foundation cross-reference |
| `/1041-review` | Form 1041 — trust return cross-reference (grantor, simple, complex) |

### CAS / Month-End Close
| Skill | Purpose |
|---|---|
| `/close` | Month-end close checklist and portfolio health check |
| `/close-summary` | Executive summary and client meeting agenda from financials |
| `/journal-entry` | Review, validate, and document journal entries |
| `/reconcile` | Bank rec, GL-to-subledger, intercompany reconciliation |
| `/fixed-assets` | Fixed asset review and depreciation schedule |

### Excel Productivity
| Skill | Purpose |
|---|---|
| `/excel/formula-refresh` | Replace hard-coded accounting export totals with SUM formulas |
| `/excel/report-format` | Standardize Excel report formatting to firm look and feel |

### Tax Planning Analysis
| Skill | Purpose |
|---|---|
| `/planning/costseg-analysis` | Screen clients for cost segregation study candidacy |
| `/planning/rd-analysis` | Screen clients for R&D tax credit study candidacy |

### Integrations
Platform-specific modules for Sage Intacct, QuickBooks Online, and Karbon. See [integrations/](integrations/).

---

## Configure for Your Firm

Add a `firm-stack` block to your project's `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Materiality threshold: $5,000
- Fiscal year-end: December 31
- GL system: QuickBooks Online
- Capitalization threshold: $2,500
- Active integrations: qbo
```

See [docs/firm-config.md](docs/firm-config.md) for all available options.

---

## Contribute

firm-stack is designed to grow with contributions from accounting professionals. See [CONTRIBUTING.md](CONTRIBUTING.md) to add a skill or improve an existing one.

---

## License

MIT — free to use, fork, and adapt.
