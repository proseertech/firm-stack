---
name: close
version: 1.0.0
description: |
  Month-end close checklist management and portfolio health check. Guides the
  manager through the close sequence — preparer tasks, manager review, director
  readiness — and surfaces blockers and at-risk clients.
trigger: |
  "month-end", "close checklist", "close status", "how is the close going",
  "portfolio health", "which clients are behind"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Close: Month-End Close Checklist & Portfolio Health

## Purpose

Drive the month-end close to completion by tracking task status, surfacing blockers, and ensuring every client reaches director-ready before the deadline.

## Required Inputs

- Client list with assigned preparer and reviewer
- Current stage for each client (or Karbon work item data)
- Business day deadline for close completion
- Any known blockers (missing bank statements, pending client responses, etc.)

## Workflow

1. **Confirm scope** — Get the list of clients in the current close cycle. Ask for current status if not provided.
2. **Assess portfolio health** — For each client, classify: On Track / At Risk / Behind. Surface the blockers for At Risk and Behind clients.
3. **Generate close checklist** — Walk through the standard close sequence for clients that are in progress:
   - Preparer: bank feed cleared, transactions coded, BS reconciliations complete, leadsheet signed off, Karbon marked complete
   - Manager: spot-check coding, review BS recs, confirm accruals/prepaids/depreciation, review P&L for anomalies, prior-period items resolved
   - Director-ready: financials packaged, executive summary drafted
4. **Identify action items** — For each blocked client, state the specific action needed and who owns it.
5. **Produce status summary** — Portfolio health table with status, blocker, and next action per client.

## Control Points

- **Missing bank statement** — Do not mark preparer stage complete without all bank accounts reconciled.
- **Prior-period open items** — Flag any prior-period items that remain unresolved at month-end.

## Red Flags

- Client has been in preparer stage for more than 5 business days without progress
- No bank activity coded for a client that normally has daily transactions
- Balance sheet reconciliation hasn't been started by day 3 of close

## Output Format

Portfolio health table:
| Client | Status | Preparer Stage | Manager Stage | Blocker | Action Required |

Plus: prioritized action list for the manager.

## Safety Constraints

- Do not mark a client as director-ready without confirming BS reconciliations are complete.
- Do not post close-related entries without preparer sign-off.
