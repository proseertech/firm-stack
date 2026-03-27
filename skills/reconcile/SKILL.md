---
name: reconcile
version: 1.0.0
description: |
  Reconcile accounts by comparing GL balances to bank statements, subledgers,
  or third-party data. Handles bank reconciliations, GL-to-subledger recs,
  and intercompany reconciliations. Identifies and categorizes reconciling items.
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

1. **Confirm scope** — Account, period, GL balance, and comparison source. Ask for what's missing.
2. **Identify timing differences** — Outstanding checks, deposits in transit, timing entries between systems. These are normal reconciling items that will clear.
3. **Identify unexplained differences** — Amounts in one source but not the other that aren't timing differences.
4. **Categorize reconciling items** — For each item: amount, description, expected resolution date, owner.
5. **Compute net difference** — GL balance +/- reconciling items = comparison source balance (or flag the remaining variance).
6. **Document the reconciliation** — Produce a formatted rec that can be saved as a workpaper.

## Control Points

- **Unexplained variance above materiality** — Any variance above the firm's materiality threshold that cannot be explained as a timing difference requires manager review before the rec is marked complete.
- **Prior-month items still outstanding** — Items that were outstanding on the prior-month rec and are still unresolved need to be flagged and investigated.

## Red Flags

- Unexplained variance that cannot be traced to a specific transaction
- Outstanding item from more than 60 days ago still unresolved
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
```

## Safety Constraints

- Do not mark a reconciliation complete with an unexplained variance above materiality.
- Do not propose journal entries to clear variances without identifying the root cause.
