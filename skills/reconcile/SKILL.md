---
name: reconcile
version: 1.4.0
description: |
  Reconcile accounts by comparing GL balances to bank statements, subledgers,
  or third-party data. Handles bank reconciliations, GL-to-subledger recs,
  and intercompany reconciliations. An account either reconciles or it
  doesn't — every difference is identified, classified as a timing item or
  unexplained variance, and tracked through to resolution.
trigger: |
  "reconcile", "bank rec", "tie out", "reconciliation", "GL to subledger",
  "intercompany rec", "accounts don't match", "help me reconcile"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Reconcile: Account Reconciliation

## Purpose

Systematically compare two sets of records to identify differences, document reconciling items, and bring accounts into agreement. Works for bank recs, GL-to-subledger, and intercompany.

## Required Inputs

- Account being reconciled (bank account name, GL account, or intercompany pair)
- GL balance as of the reconciliation date
- Comparison source: bank statement ending balance, subledger total, or counterparty balance
- Prior month reconciliation (if available)
- List of outstanding items from prior month (if available)

## Workflow

1. **Confirm scope** — Account, period, GL balance, and comparison source. An account either reconciles or it doesn't — there is no materiality threshold for reconciliation. Every difference must be identified and classified as either a timing item (will clear in a future period) or an unexplained variance (requires investigation). This applies equally to cash, AR/AP subledgers, intercompany, prepaid, and accrual accounts.
2. **Identify timing differences** — Outstanding checks, deposits in transit, timing entries between systems. These are normal reconciling items that will clear.
3. **Identify unexplained differences** — Amounts in one source but not the other that aren't timing differences.
4. **Categorize reconciling items** — For each item: amount, description, expected resolution date, owner.
5. **Aging analysis** — Categorize all outstanding items by age:
   - **Current** (0-30 days): normal, monitor
   - **Aging** (31-60 days): follow up
   - **Stale** (61-90 days): investigate
   - **Investigate** (90+ days): every item over 90 days requires a documented resolution plan regardless of amount. For bank recs, outstanding checks over 90 days may need to be voided and re-issued (subject to state unclaimed property rules).
6. **Compute net difference** — GL balance +/- reconciling items = comparison source balance (or flag the remaining variance).
7. **Document the reconciliation** — Produce a formatted rec that can be saved as a workpaper.

## Control Points

- **Unexplained variance** — Any variance that cannot be explained as a timing difference requires manager review before the rec is marked complete. There is no materiality cushion; the account either ties or it doesn't.
- **Prior-month items still outstanding** — Items that were outstanding on the prior-month rec and are still unresolved must be flagged and investigated.

## Red Flags

- Unexplained variance that cannot be traced to a specific transaction
- Outstanding item aged 90+ days without documented resolution plan
- Account type is cash but unexplained variance is non-zero
- Bank balance significantly lower than GL balance without clear explanation
- Intercompany balances that don't net to zero across entities

## Output Format

Formatted reconciliation workpaper:
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

## Safety Constraints

- Do not mark a reconciliation complete with any unexplained variance. Accounts either reconcile or they don't.
- Do not propose journal entries to clear variances without identifying the root cause.
