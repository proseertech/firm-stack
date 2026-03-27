---
name: close-summary
version: 1.1.0
description: |
  Generate an executive summary and client meeting agenda from monthly financial
  statements. Analyzes the P&L, balance sheet, and GL detail to produce a
  director-ready summary with variance analysis, key metrics, and a structured
  client meeting agenda with talking points.
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
2. **Analyze balance sheet** —
   - Ending cash and change vs. prior month; from GL detail, identify the top 3 drivers of cash increase or decrease
   - AR balance and change; AR aging summary (current vs. 30/60/90+) if aging data is available; identify key customers driving AR
   - AP balance and change vs. prior month
   - Credit cards and other current liabilities (Ramp, Amex, LOC, etc.)
   - Key fixed asset changes
   - Customer deposits / deferred revenue
   - Working capital: current assets minus current liabilities, with current ratio
3. **Analyze P&L** —
   - Total revenue and change vs. prior period
   - Gross profit and gross margin %; compare to prior period
   - Major COGS categories; identify top vendors driving COGS
   - Major OpEx categories; identify top vendors driving expenses
   - Net income and profit margin vs. prior period
   - **Variance analysis**: for each material line item, compute $ change and % change vs. prior period. Flag any variance exceeding 10% or the materiality threshold. For each flagged variance, provide:

     | Account | Current | Prior | $ Change | % Change | Explanation | Client Talking Point |
4. **Identify key vendors and transactions** — From the GL, identify which vendors are driving expenses and COGS. Flag one-time or unusual transactions: new vendors above materiality, accounts not used in prior periods, round-number amounts that may indicate estimates.
5. **Draft executive summary** — 2-4 sentence narrative covering the month's financial performance.
6. **Draft meeting agenda** — Standard 5-section structure. Each section should include 2-3 bullet talking points derived from the analysis above, not just section headers.

## Control Points

- **Unusual transactions** — Any transaction that looks like a misclassification, one-time event, or owner transaction should be flagged for director review before the summary is sent to the client.

## Red Flags

- Revenue or expenses that appear in some months but not others without explanation
- Negative cash balance or cash significantly below prior month without explanation
- AR aging shows a large overdue balance that hasn't been discussed with the client
- Cash flow doesn't match net income directionally (common for growing businesses — may indicate AR/AP timing)
- Large owner transactions or related-party entries that need disclosure context

## Output Format

```
EXECUTIVE SUMMARY
[2-4 sentence narrative]

BALANCE SHEET
- Cash: $X (change vs. prior: $X; top drivers: ...)
- AR: $X (current: $X, 30+: $X, 60+: $X, 90+: $X)
- AP: $X (change: $X)
- Credit Cards / LOC: $X
- [Other key items]

KEY METRICS
- Working Capital: $X (Current Ratio: X.X)
- Gross Margin: X.X% (prior: X.X%)
- AR Days Outstanding: X days (if data available)
- Cash Burn/Build: $X net change

PROFIT & LOSS
Gross Profit
- Revenue: $X (change: $X, X%)
- COGS: $X (margin: X%, prior margin: X%)

Expenses
- [Key categories with amounts and changes]

Net Income: $X (margin: X%, prior margin: X%)

MATERIAL VARIANCES
| Account | Current | Prior | $ Change | % Change | Explanation | Client Talking Point |

MEETING AGENDA — [Month Year] Financial Review
1. Monthly Overview
   - [2-3 talking points]
2. Balance Sheet & Working Capital
   - [2-3 talking points]
3. P&L Review
   - [2-3 talking points]
4. Operating Expenses and Process Improvements
   - [2-3 talking points]
5. Action Items & Next Steps
   - [2-3 talking points]
```

## Safety Constraints

- Do not send to client without director review.
- Do not fabricate explanations for variances — flag for discussion instead.
