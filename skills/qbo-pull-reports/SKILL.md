---
name: qbo-pull-reports
version: 1.0.0
description: |
  Pull P&L (income statement) and balance sheet from QuickBooks Online via
  the Reporting API for a specified date range and accounting method.
trigger: |
  "pull reports from QBO", "QBO P&L", "QuickBooks balance sheet",
  "get financials from QuickBooks", "export QBO reports"
allowed-tools:
  - Read
  - Bash
  - Write
  - AskUserQuestion
tier: developer
---

# QBO Pull Reports: Financial Statements from QuickBooks Online

## Purpose

Pull the profit & loss and balance sheet from QuickBooks Online for a specified period via the QBO Reporting API.

## Required Inputs

- Report type: P&L, balance sheet, or both
- Date range (start date and end date)
- Accounting method: Cash or Accrual
- QBO credentials configured in environment variables

## Workflow

1. **Confirm parameters** — Report type, date range, accounting method.
2. **Authenticate** — Use OAuth2 access token. Refresh if expired.
3. **Query reports** — Call the QBO Reports API:
   - P&L: `GET /reports/ProfitAndLoss?start_date=...&end_date=...&accounting_method=...`
   - Balance Sheet: `GET /reports/BalanceSheet?date=...&accounting_method=...`
4. **Format output** — Return structured financial statements.
5. **Save to file** (optional) — Write to CSV or Excel if requested.

## Output Format

P&L and/or balance sheet in a readable format, with section headers matching QBO's report structure.

## Safety Constraints

- Read-only — this skill only reads from QBO, never writes.
- Never store or log OAuth tokens.
