---
name: intacct-pull-tb
version: 1.0.0
description: |
  Pull a trial balance from Sage Intacct via the REST API for a specified
  period and entity. Returns account balances in a structured format suitable
  for review or import into a leadsheet.
trigger: |
  "pull trial balance from Intacct", "get Intacct TB", "Intacct trial balance",
  "export TB from Sage"
allowed-tools:
  - Read
  - Bash
  - Write
  - AskUserQuestion
tier: developer
---

# Intacct Pull TB: Trial Balance from Sage Intacct

## Purpose

Pull the trial balance for a specific period and entity from Sage Intacct, returning account balances in a structured format for review or use in a leadsheet.

## Required Inputs

- Period (year and period number, or start/end dates)
- Entity/company ID (if multi-entity)
- Intacct credentials configured in environment variables

## Workflow

1. **Confirm parameters** — Period and entity. Ask if not provided.
2. **Authenticate** — Open an Intacct API session.
3. **Query account balances** — Use the `readByQuery` function on `GLACCOUNT` or `TRIALBALANCE` object for the specified period.
4. **Format output** — Return a structured table: account number, account name, debit balance, credit balance, net balance.
5. **Save to file** (optional) — Write to CSV if requested.

## Control Points

- **Period confirmation** — Confirm the period before querying. An incorrect period could pull the wrong data into a leadsheet.

## Output Format

```
Trial Balance — [Entity] — [Period]
Account | Name | Debit | Credit | Net
101000  | Cash | 125,430.00 | | 125,430.00
...
```

Or as CSV if requested.

## Safety Constraints

- Read-only — this skill only reads from Intacct, never writes.
- Never store or log credentials.
