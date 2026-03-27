---
name: journal-entry
version: 1.0.0
description: |
  Review, validate, and document journal entries. Handles both preparer guidance
  (categorization, Dr/Cr format, one-off transactions) and manager review
  (accuracy, support, escalation routing).
trigger: |
  "journal entry", "review this JE", "post this entry", "how do I record",
  "what account does this go to", "JE review", "categorize this transaction"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Journal Entry: Review, Validate, and Document

## Purpose

Guide preparers through transaction categorization and journal entry preparation, and support managers in reviewing entries for accuracy, completeness, and proper support.

## Required Inputs

- Client name and industry
- Accounting software (QBO or Sage Intacct)
- Description of the transaction or the entry to review
- Supporting documentation if available

## Workflow

1. **Confirm context** — Client, industry, software, and transaction description.
2. **Identify transaction type** — Classify: standard expense, accrual, deferral, prepaid amortization, depreciation, payroll, intercompany, distribution, equity event, fixed asset addition, reclassification, or other.
3. **Determine account coding** — Recommend the specific account/category. Explain why.
4. **Produce the journal entry** — Format in Dr/Cr table:

   | Account | Debit | Credit | Memo |
   |---|---|---|---|

5. **Assess escalation need** — Determine if manager approval is required before posting.
6. **Document support** — Note what supporting documentation should be attached.

## Control Points

- **Manager approval required** for: materiality threshold transactions, equity/loan/distribution entries, revenue recognition questions, prior-period corrections, intercompany eliminations, tax-sensitive transactions.
- **Do not post** without explicit instruction from the preparer or manager.

## Red Flags

- 🔺 Escalate: Transaction changes a prior period
- 🔺 Escalate: Entry affects equity, loans, or distributions
- 🔺 Escalate: Amount exceeds the firm's materiality threshold
- 🔺 Escalate: Nature of the transaction is unclear and assumptions would be required

## Output Format

1. Transaction type identified
2. Recommended account coding with explanation
3. Journal entry in Dr/Cr table format
4. Escalation flag (if applicable)
5. Required supporting documentation

## Safety Constraints

- Do not post or finalize entries — output is a proposed entry for human review.
- Do not assume accounting treatment for ambiguous transactions — ask.
