---
name: intacct-import-je
version: 1.0.0
description: |
  Import one or more journal entries into Sage Intacct via the REST API.
  Accepts CSV or structured input, validates before posting, and returns
  the Intacct record IDs on success.
trigger: |
  "import journal entry to Intacct", "post to Intacct", "Intacct JE import",
  "upload journal entries to Sage"
allowed-tools:
  - Read
  - Bash
  - AskUserQuestion
tier: developer
---

# Intacct Import JE: Journal Entry Import via REST API

## Purpose

Import journal entries into Sage Intacct programmatically. Validates the entry structure before posting and returns confirmation with Intacct record keys.

## Required Inputs

- Journal entry data (CSV file or structured input): date, journal symbol, reference, debit account, credit account, amount, memo, dimensions (department, location, etc.)
- Intacct credentials configured in environment variables (see integrations/sage-intacct/README.md)
- Entity/company ID if multi-entity

## Workflow

1. **Validate credentials** — Confirm environment variables are set. Abort if missing.
2. **Parse and validate the JE** — Check that debits equal credits, required fields are present, and account codes exist in the chart of accounts format.
3. **Confirm before posting** — Show the user a summary of the entry and ask for confirmation before making the API call.
4. **Post via Intacct API** — Submit the `create_gljournalentry` XML request.
5. **Return result** — On success: Intacct record key and confirmation. On error: raw API error message and suggested fix.

## Control Points

- **Human confirmation** — Always show the full JE and ask for explicit confirmation before posting. Never auto-post.
- **Debit/credit balance** — Do not submit an unbalanced entry to the API.

## Red Flags

- Account code in the entry doesn't match the Intacct chart of accounts format
- Dimension values (department, location) that don't exist in Intacct
- Date outside the open period

## Output Format

On success:
```
Posted successfully.
Intacct Record Key: XXXXXXXX
Journal: [symbol]
Date: [date]
Amount: $X,XXX.XX
```

On error:
```
API Error: [message]
Suggested fix: [guidance]
```

## Safety Constraints

- Never post without explicit user confirmation.
- Never store or log credentials.
- If the API returns an error, do not retry automatically — surface the error to the user.
