---
name: close-summary
version: 1.2.0
description: |
  Turn a client's monthly close financials into a director-ready executive summary
  and a structured client meeting agenda. Reads the P&L, balance sheet, and GL detail
  to produce a narrative, variance analysis, key metrics, and agenda talking points.
  Use this whenever the books are closed and someone needs to package the month for
  the client — "write up the month", "executive summary", "prep for the client
  meeting", "what do I tell the client about last month", "build the monthly financial
  review", "summarize the financials for [client]". This produces the client-facing
  deliverable; it is not the close checklist itself (that's `close`).
trigger: |
  "executive summary", "close summary", "monthly summary", "financial summary",
  "client meeting prep", "prep for the client meeting", "meeting agenda",
  "package the financials", "write up the month", "summarize the financials",
  "monthly financial review", "what do I tell the client", "client-ready summary"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Close Summary: Executive Summary & Client Meeting Agenda

## Purpose

Convert a client's closed-books financials into a client-facing executive summary and a
meeting agenda the director can review before the monthly client meeting. The value is a
summary where every number is explained and every agenda line is a real talking point
grounded in the month's data — not a template of empty headers.

This assumes the books are already closed. Tracking whether the close itself is done, who's
behind, and what's blocking — that's the `close` skill. This skill packages the result.

## Required Inputs

Confirm these before analyzing. Missing GL detail is the usual gap — you can describe *what*
changed from the P&L and balance sheet, but you can't name *why* (the drivers) without it.

- Current month P&L (with prior period(s) for comparison)
- Current month balance sheet
- Current month GL detail — needed to explain cash movement and identify the vendors/customers driving AR, AP, and expenses
- Client name and industry
- Prior month summary (optional — for style/format continuity)

## Workflow

### 1. Confirm context
Client name, industry, accounting software, and the close period being summarized.

### 2. Analyze the balance sheet
- **Cash** — ending balance and change vs. prior month; from GL detail, name the top 3 drivers of the increase or decrease
- **AR** — balance and change; aging summary (current vs. 30 / 60 / 90+) if aging data is available; name the key customers driving the balance
- **AP** — balance and change vs. prior month
- **Credit cards and other current liabilities** — Ramp, Amex, LOC, etc.
- **Fixed assets** — key changes
- **Customer deposits / deferred revenue**
- **Working capital** — current assets minus current liabilities, with the current ratio

### 3. Analyze the P&L
- Total revenue and change vs. prior period
- Gross profit and gross margin %, vs. prior period
- Major COGS categories; name the top vendors driving COGS
- Major OpEx categories; name the top vendors driving expenses
- Net income and profit margin vs. prior period
- **Variance analysis** — for each material line, compute the $ and % change vs. prior period. Flag any variance over 10% or the firm materiality threshold. A raw variance isn't useful to a client on its own; each flagged line needs an explanation and something the director can actually say in the meeting:

  | Account | Current | Prior | $ Change | % Change | Explanation | Client Talking Point |

### 4. Compute key metrics
Working capital (current assets minus current liabilities), current ratio, gross margin %,
AR days outstanding (if aging data available), and net cash build/burn for the period.

### 5. Identify key vendors and unusual transactions
From the GL, name the vendors driving expenses and COGS. Flag one-time or unusual items —
new vendors above materiality, accounts not used in prior periods, round-number amounts that
may be estimates. These feed the control point in the next section.

### 6. Draft the executive summary
A 2–4 sentence narrative of the month's financial performance — the bottom line first,
then the one or two things that explain it.

### 7. Draft the meeting agenda
The standard 5-section structure below. Each section carries 2–3 talking points drawn from
the analysis above — not bare headers. An agenda that just lists section titles gives the
director nothing to prepare from.

## Control Points

- **Unusual transactions.** Anything that looks like a misclassification, a one-time event, or
  an owner/related-party transaction goes to the director for review before the summary reaches
  the client. These often need context the books don't capture, and the client will ask.

## Red Flags

Pause and surface to the user when you see:

- Revenue or expenses that appear in some months but not others, with no explanation
- A negative cash balance, or cash well below prior month, without an explanation
- AR aging showing a large overdue balance that hasn't been discussed with the client
- Cash flow that doesn't track net income directionally — common for growing businesses, and usually an AR/AP timing story worth naming
- Large owner or related-party entries that need disclosure context

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

- Do not send to the client without director review — this is an internal draft until the director signs off.
- Do not fabricate variance explanations. If you don't know why a line moved, flag it for discussion rather than inventing a reason a client might act on.
