---
name: close
version: 1.2.0
description: |
  Run the month-end close as a portfolio manager: track where every client
  stands in the close sequence (preparer → manager review → director-ready),
  surface blockers and at-risk clients, and drive each engagement to
  director-ready before the deadline. Use this whenever someone is managing or
  checking on the close across a book of clients — "where are we on close",
  "are we going to make the deadline", "what's blocking us", "which clients are
  behind", "close status", "is [client] ready to release", the daily standup, or
  the month-end push. Packaging one finished client's financials into an
  executive summary is close-summary's job; reconciling a specific account is
  reconcile's.
trigger: |
  "month-end", "close checklist", "close status", "close status update",
  "how is the close going", "where are we on close", "are we on track to close",
  "will we make the deadline", "what's blocking the close", "close blockers",
  "portfolio health", "which clients are behind", "who's behind on close",
  "is this client director-ready", "ready to release", "close push",
  "daily standup", "month-end review"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# Close: Month-End Close Checklist & Portfolio Health

## Purpose

Drive the month-end close to completion across a book of clients. The manager needs
one view of where every engagement stands, what's blocking the ones that are stuck,
and which are at risk of missing the deadline — so attention goes where it's needed
instead of spreading evenly. The skill tracks task status through the close sequence,
enforces the director-ready gate, and turns status into a prioritized action list.

Use it at any cadence — a daily spot-check, a weekly progress review, or the
month-end push.

## Scope & Handoffs

This skill manages the close *across clients* and stops at the director-ready gate. Two
adjacent jobs belong elsewhere; name the handoff rather than reproducing them here:

- Packaging one client's finished financials into an executive summary and client
  meeting agenda → **`close-summary`** (the director-ready checklist calls for this).
- Reconciling a specific account (bank, subledger, intercompany) that won't tie →
  **`reconcile`**. This skill *checks that* reconciliations are done; it doesn't do them.

## Required Inputs

Confirm these before assessing the close. If any are missing, ask — a status report
built on a stale client list or the wrong deadline sends the manager to the wrong fire.

- **Client list** with the assigned preparer and reviewer for each.
- **Current stage** for each client (preparer / manager review / director-ready), or
  the work-item data from the practice-management system (e.g. Karbon).
- **The deadline** — the business day close must be complete by.
- **Known blockers** — missing bank statements, pending client responses, etc.

## Workflow

### 1. Confirm scope

Get the list of clients in the current close cycle and each one's current stage. Ask
for status if it wasn't provided; don't assume last cycle's list still holds.

### 2. Assess portfolio health

Classify each client **On Track / At Risk / Behind**, and for anything not On Track,
name the specific blocker and its owner — that's the difference between a status report
and an action plan.

### 3. Walk the close sequence

For each in-progress client, track status against the standard sequence:

- **Preparer** — bank feed cleared, transactions coded, balance-sheet reconciliations
  complete, leadsheet signed off, work item marked complete in the practice-management
  system.
- **Manager review** — a spot-check, not a re-do:
  - Spot-check 3–5 transactions per client per period against source documents.
  - Prioritize the largest transactions, those near period-end, and those coded to
    unusual accounts — that's where errors hide.
  - For each: confirm amount, date, account coding, and supporting document.
  - Review all balance-sheet reconciliations.
  - Confirm accruals, prepaids, and depreciation are current.
  - Review the P&L for period-over-period anomalies.
  - Confirm prior-period open items are resolved.
- **Director-ready gate** — a client is director-ready only when *all* of these hold:
  - All bank accounts reconciled, with zero unexplained variance above materiality.
  - Every balance-sheet account has a current leadsheet or reconciliation.
  - P&L reviewed for period-over-period anomalies — each anomaly explained or flagged.
  - Executive summary drafted (hand off to `close-summary`).
  - All preparer and manager review notes resolved, or documented as open items.

### 4. Identify action items

For each blocked client, state the specific action needed and who owns it — not "follow
up on ABC Co." but "ABC Co.: request December bank statement from client; owner: preparer."

### 5. Produce the status summary

Deliver the portfolio health table plus the prioritized action list (see Output Format).

## Control Points

Stop and get a human decision before advancing a client past these points:

- **Missing bank statement** — don't mark the preparer stage complete until every bank
  account is reconciled; an unreconciled account can hide a misstatement that only
  surfaces after the financials go out.
- **Unresolved prior-period open items** — flag any that remain at month-end rather than
  rolling them silently into the new period.
- **Director-ready gate** — don't mark a client director-ready unless every criterion in
  Step 3 is met. This gate is what stands between the manager's review and release to the
  director; skipping a criterion defeats the review.

## Red Flags

Pause and surface to the manager when:

- A client has sat in the preparer stage more than 5 business days without progress.
- No bank activity is coded for a client that normally has daily transactions —
  suggests the feed didn't sync or the work hasn't started.
- Balance-sheet reconciliation hasn't been started by day 3 of the close.
- A balance-sheet reconciliation variance exceeds materiality with no documented
  explanation.

## Output Format

**Portfolio health table:**

| Client | Close Health | Preparer Stage | Manager Stage | Blockers | Action Required | Days in Stage |

**Prioritized action list** for the manager, ordered by urgency — the Behind and At Risk
clients first, each with the specific next action and its owner.

## Safety Constraints

- Do not mark a client director-ready without confirming balance-sheet reconciliations
  are complete and every director-ready criterion is met — that flag tells the director
  the file is releasable.
- Do not post close-related entries without preparer sign-off; the preparer owns the
  work paper the entry rests on.
