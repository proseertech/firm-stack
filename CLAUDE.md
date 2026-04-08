# firm-stack

A Claude Code plugin for accounting firms. This file registers all available skills and describes how to configure them for your firm.

---

## Available Skills

### Client Communications
- **`/firm-stack:client-email`** — Polish a CPA-to-client email draft. Trigger: "improve this email", "polish my draft", "client email"
- **`/firm-stack:tax-memo`** — Draft a client-facing tax memo from position notes. Trigger: "tax memo", "client memo", "write a memo"

### Tax Workflow
- **`/tax-info-request`** — Generate an information request from a prior year 1040. Trigger: "information request", "info request", "tax organizer", "document request list"
- **`/firm-stack:tax-workpapers`** — Build Excel workpapers summarizing 1099s and K-1s for any return type (1040, 1065, 1120-S, 1041). Trigger: "tax workpapers", "1099 summary", "K-1 summary", "build the workpapers", "partnership workpapers"

### Tax Return Reviews
- **`/firm-stack:1040-review`** — Cross-reference a Form 1040 against source documents. Trigger: "review the 1040", "check the individual return", "1040 cross-reference"
- **`/firm-stack:1120s-review`** — Cross-reference a Form 1120-S against source documents. Trigger: "review the 1120-S", "S-corp return review", "check the S-corp"
- **`/firm-stack:1120-review`** — Cross-reference a Form 1120 against source documents. Trigger: "review the 1120", "C-corp return review"
- **`/firm-stack:1065-review`** — Cross-reference a Form 1065 against source documents. Trigger: "review the 1065", "partnership return review", "check the K-1s"
- **`/firm-stack:990-review`** — Cross-reference a Form 990-PF against source documents. Trigger: "review the 990", "private foundation return", "990-PF review"
- **`/firm-stack:1041-review`** — Cross-reference a Form 1041 against source documents. Trigger: "review the 1041", "trust return review", "grantor trust", "fiduciary return"

### CAS / Month-End Close
- **`/firm-stack:close`** — Month-end close checklist and portfolio health check. Trigger: "month-end", "close checklist", "close status"
- **`/firm-stack:close-summary`** — Executive summary and client meeting agenda from financials. Trigger: "executive summary", "client meeting prep", "close summary", "monthly summary"
- **`/firm-stack:journal-entry`** — Review, validate, and document journal entries. Trigger: "journal entry", "review this JE", "post this entry"
- **`/firm-stack:reconcile`** — Reconcile bank, GL-to-subledger, or intercompany. Trigger: "reconcile", "bank rec", "tie out", "reconciliation"
- **`/firm-stack:fixed-assets`** — Fixed asset review and depreciation schedule. Trigger: "fixed assets", "depreciation", "capitalize or expense", "R&M review"

### Excel Productivity
- **`/firm-stack:excel-formula-refresh`** — Replace hard-coded totals in an accounting export with SUM formulas. Trigger: "formula refresh", "fix the totals", "add SUM formulas", "hard-coded export"
- **`/firm-stack:excel-report-format`** — Standardize Excel report formatting to firm look and feel. Trigger: "format this report", "standardize this Excel", "apply firm formatting"

### Tax Planning & Projections
- **`/firm-stack:tax-projection-estimate`** — Build a standardized tax projection for a 1065 or 1120S from any GL trial balance and prior-year return. Tags every TB account, uses SUMIF-linked formulas, produces K-1 allocation by line item per partner/shareholder. Trigger: "tax projection", "tax estimate", "K-1 estimate", "estimate taxable income"
- **`/firm-stack:costseg-analysis`** — Screen a client for cost segregation study candidacy. Trigger: "cost seg", "cost segregation", "bonus depreciation candidate", "should we do a cost seg"
- **`/firm-stack:rd-analysis`** — Screen a client for R&D tax credit study candidacy. Trigger: "R&D credit", "research credit", "should we do an R&D study", "179 research"

### Integrations
- **`/firm-stack:intacct-import-je`** — Import journal entries via Sage Intacct REST API. Trigger: "import JE to Intacct", "post to Intacct"
- **`/firm-stack:intacct-pull-tb`** — Pull trial balance from Sage Intacct. Trigger: "pull TB from Intacct", "Intacct trial balance"
- **`/firm-stack:qbo-pull-reports`** — Pull P&L and balance sheet from QuickBooks Online. Trigger: "pull QBO reports", "QBO P&L", "QBO balance sheet"
- **`/firm-stack:karbon-work-status`** — Query and update Karbon work item status. Trigger: "Karbon status", "work item status", "update Karbon"

---

## Firm Configuration

### Plugin Config (recommended)

When you install firm-stack as a plugin, you'll be prompted for firm-specific settings:
- Materiality threshold
- GL system
- Tax software
- Fiscal year-end
- Capitalization threshold

These values are stored in your plugin config and available to all skills automatically.

### Manual Config (fallback)

If not using the plugin install, add this block to your **project's** `CLAUDE.md`:

```markdown
## firm-stack Configuration
- Materiality threshold: $X,XXX
- Fiscal year-end: [Month DD]
- GL system: [Sage Intacct | QBO | NetSuite | Xero | Other]
- Capitalization threshold: $X,XXX
- Active integrations: [sage-intacct, qbo, karbon]
- Tax software: [Lacerte | ProSystem | Drake | UltraTax | Other]
- Return types: [1040, 1120S, 1120, 1065, 990PF, 1041]
```

If no config is present, skills will prompt the user for required context before proceeding.

---

## Installation

### As a Plugin (recommended)

```
/plugin marketplace add larryb821/firm-stack
/plugin install firm-stack@firm-stack
```

### As a Skills Pack (legacy)

```bash
git clone https://github.com/larryb821/firm-stack ~/.claude/skills/firm-stack
```

### Org-Level (Claude Desktop admin)

Individual SKILL.md files can be uploaded via Organization Settings > Skills in Claude Desktop.

---

## Adding Skills

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/skill-authoring.md](docs/skill-authoring.md).
