---
name: reconcile
version: 1.5.0
description: |
  Reconcile a GL account to an independent source — bank statement, subledger,
  or a counterparty's books — and drive every difference to a documented
  resolution. Covers bank reconciliations, GL-to-subledger recs (AR, AP, prepaid,
  accruals, inventory), and intercompany recs. Use this whenever an account needs
  to be tied out and it isn't the whole-close checklist: "reconcile the bank," "why
  doesn't cash tie," "the AP subledger doesn't match the GL," "tie out prepaids,"
  "our intercompany doesn't net to zero," "clean up this bank rec," or "I have a
  variance I can't explain." An account either reconciles or it doesn't — there is
  no materiality cushion, so reach for this even for small differences that won't
  clear.
trigger: |
  "reconcile", "reconciliation", "bank rec", "tie out", "tie it out",
  "GL to subledger", "subledger doesn't match", "AP doesn't match the GL",
  "AR reconciliation", "intercompany rec", "intercompany doesn't net",
  "accounts don't match", "cash doesn't tie", "why doesn't this tie",
  "unexplained variance", "clean up the bank rec", "help me reconcile"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Reconcile: Account Reconciliation

## Purpose

Compare a GL account against an independent record, identify every difference, and
classify each as either a timing item that will clear or an unexplained variance that
must be investigated — then document the result as a workpaper. Works for bank recs,
GL-to-subledger recs, and intercompany recs.

The defining principle: **an account either reconciles or it doesn't.** Unlike analytical
work, reconciliation has no materiality threshold — a $12 unexplained difference is as much
a break as a $12,000 one, because an unexplained difference of any size means you don't yet
know what's in the account. Every difference gets identified and driven to resolution.

## Scope & Handoffs

This skill ties out **one account (or intercompany pair) at a time**. If the user wants a
month-end close checklist or a portfolio-wide status across many accounts, that's the
**`close`** skill — reconciliation is one line on its checklist. Do the tie-out here; hand
back to `close` for overall close status.

## Required Inputs

Confirm before starting — a rec built on the wrong balance or period looks clean but ties
nothing:

- Account being reconciled (bank account name, GL account, or intercompany pair)
- GL balance as of the reconciliation date
- Comparison source: bank statement ending balance, subledger total, or counterparty balance
- Prior-month reconciliation, if available
- List of outstanding items from the prior month, if available

## Workflow

1. **Confirm scope** — Account, period, GL balance, and comparison source. Restate what you're
   tying to what, so a wrong-source rec doesn't get built. The same discipline applies to every
   account type — cash, AR/AP subledgers, intercompany, prepaid, and accrual.
2. **Identify timing differences** — Outstanding checks, deposits in transit, entries booked in
   one system before the other. These are normal reconciling items expected to clear in a future
   period.
3. **Identify unexplained differences** — Amounts in one source but not the other that are *not*
   timing items. These are the breaks that keep the account from tying and must be run down to a
   specific transaction.
4. **Categorize each reconciling item** — Amount, description, expected resolution date, owner.
5. **Age the outstanding items** — Bucket every outstanding item by age:
   - **Current** (0–30 days): normal, monitor
   - **Aging** (31–60 days): follow up
   - **Stale** (61–90 days): investigate
   - **Investigate** (90+ days): needs a documented resolution plan regardless of amount. For
     bank recs, outstanding checks over 90 days may need to be voided and re-issued — subject to
     state unclaimed property (escheatment) rules, so confirm before voiding.
6. **Compute the net difference** — GL balance +/- reconciling items = comparison source balance.
   If anything is left over, that remainder is an unexplained variance — flag it; don't bury it.
7. **Document the reconciliation** — Produce a formatted rec that can be saved as a workpaper.

## Control Points

Stop and get a human decision before marking the rec complete when:

- **An unexplained variance remains** — Any difference that can't be explained as a timing item
  requires manager review before the rec is closed. There is no materiality cushion; a rec that
  still has an unexplained break is not a completed rec, no matter how small the number.
- **A prior-month item is still outstanding** — Items that were on the prior-month rec and haven't
  cleared must be flagged and investigated. Items that never clear are how errors and fraud hide
  in a rec that otherwise "foots."

## Red Flags

Pause and surface to the user when you see:

- An unexplained variance that can't be traced to a specific transaction
- An outstanding item aged 90+ days with no documented resolution plan
- A cash account with a non-zero unexplained variance (cash should tie to the penny)
- A bank balance materially below the GL balance with no clear explanation (possible overdraft,
  unrecorded withdrawals, or fraud)
- Intercompany balances that don't net to zero across entities

## Output Format

A formatted reconciliation workpaper:

```
Account: [Name]           Period: [Month Year]
GL Balance:               $X,XXX
Reconciling Items:
  [Description]           $(X,XXX)
  [Description]           $X,XXX
Adjusted Balance:         $X,XXX
Comparison Source:        $X,XXX
Unexplained Variance:     $0

OUTSTANDING ITEMS AGING
| Item | Amount | Age (Days) | Category | Action Required |
```

Each reconciling item names a specific amount and transaction; each aged item names the action
required and who owns it.

## Safety Constraints

- **Do not mark a reconciliation complete while any unexplained variance remains.** A rec that
  doesn't tie to zero isn't done — closing it hides the break instead of resolving it.
- **Do not propose a journal entry to clear a variance without first identifying the root cause.**
  A plug that makes the account foot without explaining the difference converts a known unknown
  into an undetectable error.
