---
name: close-summary
version: 1.0.0
description: |
  Generate an executive summary and client meeting agenda from monthly financial
  statements. Analyzes the P&L, balance sheet, and GL detail to produce a
  director-ready summary and a structured client meeting agenda.
trigger: |
  "executive summary", "client meeting prep", "close summary", "monthly summary",
  "financial summary", "meeting agenda", "package the financials"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Close Summary: Executive Summary & Client Meeting Agenda

## Purpose

Convert the close financials into a structured client-facing summary and a meeting agenda. The summary goes to the accounting director for review before the client meeting.

## Required Inputs

- Current month P&L (may include prior periods)
- Current month balance sheet
- Current month GL detail (for cash, AR, AP, and key expense analysis)
- Prior month summary (optional, for style reference)
- Client name and industry

## Workflow

1. **Confirm context** — Client name, industry, accounting software, current close period.
2. **Analyze balance sheet** — Ending cash and change vs. prior month; AR and key customer drivers; AP and change; credit cards/other current liabilities; fixed asset changes; customer deposits/deferred revenue; current ratio.
3. **Analyze P&L** — Total revenue and change; gross profit and margin; COGS drivers; major OpEx categories; net income and profit margin.
4. **Identify key vendors and transactions** — From the GL, identify which vendors are driving expenses and COGS. Flag one-time or unusual transactions.
5. **Draft executive summary** — 2-4 sentence narrative covering the month.
6. **Draft meeting agenda** — Standard structure: Monthly Overview, Balance Sheet & Working Capital, P&L Review, Operating Expenses and Process Improvements, Action Items & Next Steps.

## Control Points

- **Unusual transactions** — Any transaction that looks like a misclassification, one-time event, or owner transaction should be flagged for director review before the summary is sent to the client.

## Red Flags

- Revenue or expenses that appear in some months but not others without explanation
- Negative cash balance or cash significantly below prior month without explanation
- AR aging shows a large overdue balance that hasn't been discussed with the client

## Output Format

```
EXECUTIVE SUMMARY
[2-4 sentence narrative]

BALANCE SHEET
- Cash: $X (change vs. prior: $X)
- AR: $X (key customers: ...)
- AP: $X (change: $X)
- [Other key items]

PROFIT & LOSS
Gross Profit
- Revenue: $X
- COGS: $X (margin: X%)

Expenses
- [Key categories with amounts]

Net Income: $X (margin: X%)

MEETING AGENDA — [Month Year] Financial Review
1. Monthly Overview
2. Balance Sheet & Working Capital
3. P&L Review
4. Operating Expenses and Process Improvements
5. Action Items & Next Steps
```

## Safety Constraints

- Do not send to client without director review.
- Do not fabricate explanations for variances — flag for discussion instead.
