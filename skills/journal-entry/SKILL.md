---
name: journal-entry
version: 1.1.0
description: |
  Review, validate, and document journal entries. Handles both preparer guidance
  (categorization, Dr/Cr format, one-off transactions) and manager review
  (accuracy, support, escalation routing). Validates against chart of accounts
  when available and flags multi-entity and revenue recognition considerations.
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
- Chart of accounts or account list (if available)
- Entity name if multi-entity client

## Workflow

1. **Confirm context** — Client, industry, software, entity (if multi-entity), and transaction description.
2. **Identify transaction type** — Classify: standard expense, accrual, deferral, prepaid amortization, depreciation, payroll, intercompany, distribution, equity event, fixed asset addition, reclassification, or other. If the transaction is a revenue event and the client has contracts, flag ASC 606 applicability: "This revenue transaction may require ASC 606 analysis if performance obligations span multiple periods. Confirm with manager."
3. **Determine account coding** — Recommend the specific account/category. If a chart of accounts is provided, validate the recommended account exists; if it doesn't, note that the account may need to be created. For each recommendation, state the accounting rationale — explain *why* this account is correct (e.g., "Coded to 6200 - Professional Fees because this is a recurring legal retainer, not a one-time litigation cost which would go to 6210 - Legal Expenses").
4. **Multi-entity check** — If the client has multiple entities and the transaction involves an intercompany element, flag it. Provide the entries needed on both sides. Reference the elimination entry needed at consolidation if applicable.
5. **Produce the journal entry** — Format in Dr/Cr table:

   | Account | Debit | Credit | Memo |
   |---|---|---|---|

6. **Assess escalation need** — Determine if manager approval is required before posting.
7. **Document support** — Note what supporting documentation should be attached.

## Control Points

- **Manager approval required** for: materiality threshold transactions, equity/loan/distribution entries, revenue recognition questions, prior-period corrections, intercompany eliminations, tax-sensitive transactions.
- **Do not post** without explicit instruction from the preparer or manager.

## Red Flags

- 🔺 Escalate: Transaction changes a prior period
- 🔺 Escalate: Entry affects equity, loans, or distributions
- 🔺 Escalate: Amount exceeds the firm's materiality threshold
- 🔺 Escalate: Nature of the transaction is unclear and assumptions would be required
- 🔺 Escalate: Revenue recognition — transaction involves a multi-period contract or milestone billing
- 🔺 Escalate: Multi-entity — transaction has an intercompany component requiring matching entries

## Output Format

1. Transaction type identified
2. Recommended account coding with accounting rationale
3. Journal entry in Dr/Cr table format (both sides if intercompany)
4. Escalation flag (if applicable)
5. Required supporting documentation

## Safety Constraints

- Do not post or finalize entries — output is a proposed entry for human review.
- Do not assume accounting treatment for ambiguous transactions — ask.
