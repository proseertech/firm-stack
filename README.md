# firm-stack

**Claude Code plugin for accounting firms.**

A collection of skills that extend Claude with accounting-specific workflows — tax return review, month-end close, reconciliation, client communications, and more. Built by [Proseer](https://proseer.co), designed for any CPA or accounting firm.

Inspired by [gstack](https://github.com/garrytan/gstack) and [superpowers](https://github.com/obra/superpowers).

---

## Install

### As a Plugin (recommended)

```
/plugin marketplace add larryb821/firm-stack
/plugin install firm-stack@firm-stack
```

Skills are namespaced as `/firm-stack:<skill-name>` and available in Claude Code, Claude Desktop, and IDE extensions.

### As Org-Level Skills (Claude Desktop)

Admins can upload individual SKILL.md files via **Organization Settings > Skills** in the Claude Desktop app. No terminal required.

### As a Skills Pack (legacy)

```bash
git clone https://github.com/larryb821/firm-stack ~/.claude/skills/firm-stack
```

---

## Skills

### Client Communications
| Skill | Purpose |
|---|---|
| `client-email` | Polish CPA-to-client email drafts |
| `tax-memo` | Draft client-facing tax memos from position notes |

### Tax Workflow
| Skill | Purpose |
|---|---|
| `/tax-info-request` | Generate a document request list from a prior year 1040 |

### Tax Return Reviews
| Skill | Purpose |
|---|---|
| `1040-review` | Form 1040 — individual return cross-reference |
| `1120s-review` | Form 1120-S — S-corp return cross-reference |
| `1120-review` | Form 1120 — C-corp return cross-reference |
| `1065-review` | Form 1065 — partnership return cross-reference |
| `990-review` | Form 990-PF — private foundation cross-reference |
| `1041-review` | Form 1041 — trust return cross-reference (grantor, simple, complex) |

### CAS / Month-End Close
| Skill | Purpose |
|---|---|
| `close` | Month-end close checklist and portfolio health check |
| `close-summary` | Executive summary and client meeting agenda from financials |
| `journal-entry` | Review, validate, and document journal entries |
| `reconcile` | Bank rec, GL-to-subledger, intercompany reconciliation |
| `fixed-assets` | Fixed asset review and depreciation schedule |

### Excel Productivity
| Skill | Purpose |
|---|---|
| `excel-formula-refresh` | Replace hard-coded accounting export totals with SUM formulas |
| `excel-report-format` | Standardize Excel report formatting to firm look and feel |

### Tax Planning Analysis
| Skill | Purpose |
|---|---|
| `costseg-analysis` | Screen clients for cost segregation study candidacy |
| `rd-analysis` | Screen clients for R&D tax credit study candidacy |

### Integrations
| Skill | Platform | Purpose |
|---|---|---|
| `intacct-import-je` | Sage Intacct | Import journal entries via REST API |
| `intacct-pull-tb` | Sage Intacct | Pull trial balance via REST API |
| `qbo-pull-reports` | QuickBooks Online | Pull P&L and balance sheet |
| `karbon-work-status` | Karbon | Query and update work item status |

Integration setup instructions: [Sage Intacct](integrations/sage-intacct/README.md) | [QBO](integrations/qbo/README.md) | [Karbon](integrations/karbon/README.md)

---

## Configure for Your Firm

When installed as a plugin, you'll be prompted for firm-specific settings (materiality threshold, GL system, tax software, etc.).

For manual configuration, add a `firm-stack Configuration` block to your project's `CLAUDE.md`. See [docs/firm-config.md](docs/firm-config.md) for all options.

---

## Contribute

firm-stack is designed to grow with contributions from accounting professionals. See [CONTRIBUTING.md](CONTRIBUTING.md) to add a skill or improve an existing one.

---

## License

MIT — free to use, fork, and adapt.
