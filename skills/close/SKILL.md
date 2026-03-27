---
name: close
version: 1.1.0
description: |
  Month-end close checklist management and portfolio health check. Guides the
  manager through the close sequence — preparer tasks, manager review, director
  readiness — and surfaces blockers and at-risk clients. Defines director-ready
  criteria explicitly and includes a spot-check methodology for manager review.
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

Drive the month-end close to completion by tracking task status, surfacing blockers, and ensuring every client reaches director-ready before the deadline. This skill can be used at any cadence — daily spot-checks, weekly progress reviews, or month-end close push.

## Required Inputs

- Client list with assigned preparer and reviewer
- Current stage for each client (or Karbon work item data)
- Business day deadline for close completion
- Any known blockers (missing bank statements, pending client responses, etc.)

## Workflow

1. **Confirm scope** — Get the list of clients in the current close cycle. Ask for current status if not provided.
2. **Assess portfolio health** — For each client, classify: On Track / At Risk / Behind. Surface the blockers for At Risk and Behind clients.
3. **Generate close checklist** — Walk through the standard close sequence for clients that are in progress:
   - **Preparer**: bank feed cleared, transactions coded, BS reconciliations complete, leadsheet signed off, Karbon marked complete
   - **Manager review** — includes a spot-check methodology:
     - Spot-check 3-5 transactions per client per period against source documents
     - Prioritize: largest transactions, transactions near period-end, transactions coded to unusual accounts
     - For each spot-check: confirm amount, date, account coding, and supporting document
     - Review all BS reconciliations
     - Confirm accruals/prepaids/depreciation are current
     - Review P&L for period-over-period anomalies
     - Confirm prior-period open items are resolved
   - **Director-ready** — all of the following must be true:
     - All bank accounts reconciled with zero unexplained variance above materiality
     - All balance sheet accounts have a current leadsheet or reconciliation
     - P&L reviewed for period-over-period anomalies — anomalies either explained or flagged
     - Executive summary drafted (can invoke `/close-summary`)
     - All preparer and manager review notes resolved or documented as open items
4. **Identify action items** — For each blocked client, state the specific action needed and who owns it.
5. **Produce status summary** — Portfolio health table with status, blocker, next action, and days in current stage per client.

## Control Points

- **Missing bank statement** — Do not mark preparer stage complete without all bank accounts reconciled.
- **Prior-period open items** — Flag any prior-period items that remain unresolved at month-end.
- **Director-ready gate** — Do not mark a client as director-ready unless all criteria in Step 3 are met.

## Red Flags

- Client has been in preparer stage for more than 5 business days without progress
- No bank activity coded for a client that normally has daily transactions
- Balance sheet reconciliation hasn't been started by day 3 of close
- Balance sheet reconciliation variance exceeds materiality without documented explanation

## Output Format

Portfolio health table:
| Client | Close Health | Preparer Stage | Manager Stage | Blockers | Action Required | Days in Stage |

Plus: prioritized action list for the manager, ordered by urgency.

## Safety Constraints

- Do not mark a client as director-ready without confirming BS reconciliations are complete and all director-ready criteria are met.
- Do not post close-related entries without preparer sign-off.
