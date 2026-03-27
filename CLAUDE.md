# firm-stack

A Claude Code skills pack for accounting firms. This file registers all available skills and describes how to configure them for your firm.

---

## Available Skills

### Client Communications
- **`/client-email`** — Polish a CPA-to-client email draft. Trigger: "improve this email", "polish my draft", "client email"
- **`/tax-memo`** — Draft a client-facing tax memo from position notes. Trigger: "tax memo", "client memo", "write a memo"

### Tax Workflow
- **`/tax-info-request`** — Generate an information request from a prior year 1040. Trigger: "information request", "info request", "tax organizer", "document request list"

### Tax Return Reviews
- **`/1040-review`** — Cross-reference a Form 1040 against source documents. Trigger: "review the 1040", "check the individual return", "1040 cross-reference"
- **`/1120s-review`** — Cross-reference a Form 1120-S against source documents. Trigger: "review the 1120-S", "S-corp return review", "check the S-corp"
- **`/1120-review`** — Cross-reference a Form 1120 against source documents. Trigger: "review the 1120", "C-corp return review"
- **`/1065-review`** — Cross-reference a Form 1065 against source documents. Trigger: "review the 1065", "partnership return review", "check the K-1s"
- **`/990-review`** — Cross-reference a Form 990-PF against source documents. Trigger: "review the 990", "private foundation return", "990-PF review"
- **`/1041-review`** — Cross-reference a Form 1041 against source documents. Trigger: "review the 1041", "trust return review", "grantor trust", "fiduciary return"

### CAS / Month-End Close
- **`/close`** — Month-end close checklist and portfolio health check. Trigger: "month-end", "close checklist", "close status"
- **`/close-summary`** — Executive summary and client meeting agenda from financials. Trigger: "executive summary", "client meeting prep", "close summary", "monthly summary"
- **`/journal-entry`** — Review, validate, and document journal entries. Trigger: "journal entry", "review this JE", "post this entry"
- **`/reconcile`** — Reconcile bank, GL-to-subledger, or intercompany. Trigger: "reconcile", "bank rec", "tie out", "reconciliation"
- **`/fixed-assets`** — Fixed asset review and depreciation schedule. Trigger: "fixed assets", "depreciation", "capitalize or expense", "R&M review"

### Excel Productivity
- **`/excel/formula-refresh`** — Replace hard-coded totals in an accounting export with SUM formulas. Trigger: "formula refresh", "fix the totals", "add SUM formulas", "hard-coded export"
- **`/excel/report-format`** — Standardize Excel report formatting to firm look and feel. Trigger: "format this report", "standardize this Excel", "apply firm formatting"

### Tax Planning Analysis
- **`/planning/costseg-analysis`** — Screen a client for cost segregation study candidacy. Trigger: "cost seg", "cost segregation", "bonus depreciation candidate", "should we do a cost seg"
- **`/planning/rd-analysis`** — Screen a client for R&D tax credit study candidacy. Trigger: "R&D credit", "research credit", "should we do an R&D study", "179 research"

---

## Firm Configuration

Add the following block to your **project's** `CLAUDE.md` (not this file) to customize skill behavior for your firm:

```markdown
## firm-stack Configuration
- Materiality threshold: $X,XXX         # Auto-fix below this amount; ask above it
- Fiscal year-end: [Month DD]
- GL system: [Sage Intacct | QBO | NetSuite | Xero | Other]
- Capitalization threshold: $X,XXX
- Active integrations: [sage-intacct, qbo, karbon]
- Tax software: [Lacerte | ProSystem | Drake | UltraTax | Other]
- Return types: [1040, 1120S, 1120, 1065, 990PF, 1041]
```

If no firm config is present, skills will prompt the user for required context before proceeding.

---

## Installation

```bash
git clone https://github.com/larryb821/firm-stack ~/.claude/skills/firm-stack
```

Skills are then available as slash commands in any Claude Code session.

---

## Adding Skills

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/skill-authoring.md](docs/skill-authoring.md).
