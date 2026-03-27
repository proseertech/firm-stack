---
name: tax-info-request
version: 1.0.0
description: |
  Review a prior year individual tax return (Form 1040) PDF and generate a
  structured information request for the current tax year. Extracts every
  income source, deduction, entity, and account from the return, then produces
  a client-ready document request organized by category with prior year
  reference amounts.
trigger: |
  "information request", "info request", "tax organizer", "review prior year return",
  "document request list", "what do we need from the client", "1040 info request"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: all-staff
---

# Tax Info Request: Prior Year Return → Document Request

## Purpose

Generate a complete, client-ready information request for the upcoming tax year by extracting every relevant item from the prior year Form 1040. The output lists exactly what documents the client needs to provide, organized by category, with prior year reference amounts for context. This replaces the manual process of paging through a return and building a request from scratch.

## Required Inputs

- Path to the prior year tax return PDF
- Override notes from the user (optional) — e.g., "skip rental section", "add crypto question", "they sold the property", "new baby born in 2025"

## Workflow

1. **Read the full return** — Read the tax return PDF in batches of 20 pages. Read ALL pages — K-1 details, state returns, and supporting statements are often at the end. Do not stop early.

2. **Extract the checklist** — Systematically extract data from every section of the return:

   **A. Form 1040 — Basic Information**
   - Tax year, taxpayer name(s), filing status, home address
   - Number and names of dependents with relationships
   - Digital assets question (Yes/No)

   **B. Form 1040 — Income Lines**
   - Line 1: Wages/salaries (W-2)
   - Lines 2a/2b: Tax-exempt and taxable interest
   - Lines 3a/3b: Qualified and ordinary dividends
   - Lines 4a/4b: IRA distributions
   - Lines 5a/5b: Pensions and annuities
   - Lines 6a/6b: Social security benefits
   - Line 7: Capital gain/loss
   - Line 8: Additional income (Schedule 1 — rental, partnership, K-1, etc.)
   - Line 12: Itemized or standard deduction amount
   - Line 13: QBI deduction

   **C. Schedule B — Interest and Dividends**
   - Part I: Each interest payer with name and account identifier
   - Part II: Each dividend payer with name and account identifier
   - Part III, Line 7a: Foreign accounts question (Yes/No); if Yes, note foreign bank names, account numbers, countries
   - Part III, Line 8: Foreign trust question (Yes/No)

   **D. Schedule D / Form 8949 — Capital Gains**
   - Brokerage accounts appearing on Form 8949 (names + account fragments)
   - Whether crypto/digital assets appear in transactions
   - Short-term vs. long-term activity

   **E. Schedule E — Supplemental Income**
   - Part I (Rental): Each property address, type, income, expense categories, rental/personal use days
   - Part II (Pass-throughs): Each entity name, EIN, type (P or S), passive/nonpassive, income amounts

   **F. Schedule A — Itemized Deductions**
   - Whether taxpayer itemizes; if so: medical, state/local taxes, real estate taxes, mortgage interest, investment interest, charitable (cash and non-cash), other

   **G. Estimated Tax Payments**
   - Payments made during the year (Line 26)
   - Overpayment applied to next year (Line 36)
   - Estimated payment voucher amounts (if 1040-ES worksheets present)

   **H. Other Forms Present**
   - Form 1116 (Foreign Tax Credit), Form 8960 (NIIT), Form 8995 (QBI), Form 4797 (Sale of Business Property), Form 6251 (AMT), Form 2441 (Child Care), Form 8863 (Education Credits), Schedule C, Schedule SE, Schedule H, state returns, W-2 employer names

   **I. Supporting Statements**
   - Supplemental statements detailing interest, dividends, partnerships, rental expenses, or other breakdowns

3. **Apply user overrides** — If the user provided override notes:
   - "Skip [section]" — omit that section from the output
   - "Add [topic]" — add a custom question or section
   - "They sold [property]" — note the property is no longer applicable but ask about sale details (1099-S, closing statement)
   - "New [life event]" — add relevant questions (new dependent, marriage, divorce, new home, etc.)

4. **Generate the information request** — Produce the output using the template below. Only include sections where the prior year return shows relevant activity or where user overrides add something.

## Control Points

- **Sensitive client data** — The output will contain client names, addresses, EINs, and account fragments. Confirm the output destination (file path, email draft, etc.) before writing.
- **Missing pages** — If the PDF appears incomplete (e.g., no page 2 of Form 1040, or K-1s referenced but not included), flag what appears to be missing before generating the request.

## Red Flags

- Return references K-1 entities but no K-1s are included in the PDF — note which entities are expected
- Foreign accounts question answered Yes but no FBAR/FATCA details visible — flag for follow-up
- Large estimated tax payments that may indicate underwithholding pattern — include in the request
- Digital assets question answered Yes but no Schedule D/Form 8949 crypto activity — ask about current year activity

## Output Format

Plain-text, client-ready document organized with clear section headers:

```
============================================================
[CURRENT YEAR] TAX INFORMATION REQUEST
============================================================
Prepared for: [Taxpayer Name(s)]
Based on review of [Prior Year] Federal Tax Return
Filing Status: [MFJ/Single/etc.]
------------------------------------------------------------

PERSONAL INFORMATION
- Please confirm your current home address:
  [Address from prior year return]
- Please confirm filing status for [current year]: [status]
- Dependents reported on prior year return:
  [List each: Name — Relationship]
  Are all dependents still claimed? Any new dependents?

------------------------------------------------------------

FOREIGN BANK ACCOUNTS
[Only if Schedule B Part III = Yes]

[For each known foreign account:]
- [Bank Name] — Acct [last 4 digits]
  * Highest account balance during [current year]
  * Interest income earned from this account

- Any other foreign bank accounts during [current year]?

Note: FBAR (FinCEN 114) filing may be required if aggregate
balance of all foreign accounts exceeded $10,000 at any time.

------------------------------------------------------------

WAGES & EMPLOYMENT (W-2)
[Only if wages present]

[List each employer from W-2s:]
- Please provide [current year] W-2 from [Employer Name]

- Did you have any new employers or change jobs?

------------------------------------------------------------

BANK / INVESTMENT ACCOUNTS — Please share 1099s
[List every payer from Schedule B + brokerage from 8949]

[Group by institution:]
- [Institution] — Acct [last 4]
- [Institution] — Acct [last 4]

Please let us know if you have any accounts not listed above.

------------------------------------------------------------

PARTNERSHIP / S-CORP INCOME (K-1s)
[Only if Schedule E Part II has entries]

We expect Schedule K-1 forms from the following entities.
Please forward as you receive them:

- [Entity Name] (EIN: [##-#######])

Please let us know if you have K-1s from entities not
listed above, or if you are no longer involved in any.

------------------------------------------------------------

RENTAL INCOME
[Only if Schedule E Part I has entries]

[For each rental property:]
- [Property Address]
  Prior year rental income: $[amount]
  Please provide:
  * Gross rental income for [current year]
  * Expenses: maintenance/repairs, HOA, real estate taxes,
    utilities, insurance, management fees, other

------------------------------------------------------------

CAPITAL GAINS / DIGITAL ASSETS
[Only if Schedule D / Form 8949 has activity]

[If digital assets = Yes:]
- Did you buy, sell, or exchange any cryptocurrency or
  digital assets in [current year]?

[If brokerage activity:]
- 1099-B forms should be included with your brokerage
  1099 composite statements listed above.

------------------------------------------------------------

ITEMIZED DEDUCTIONS
[Only if Schedule A was used]

Please provide for [current year]:

[If real estate taxes > 0:]
- Property tax bills/statements (prior year: $[amount])

[If mortgage interest / Form 1098:]
- Form 1098 — Mortgage Interest Statement

[If charitable > 0:]
- Charitable contribution receipts, cash and non-cash
  (prior year cash donations: $[amount])

[If medical > 0:]
- Summary of medical and dental expenses paid
  (prior year: $[amount])

[If investment interest > 0:]
- Investment interest expense documentation

------------------------------------------------------------

ESTIMATED TAX PAYMENTS
[Only if estimated payments were made or vouchers generated]

Prior year estimated payments: $[total]
[If overpayment applied:] Overpayment of $[amount] was
applied to [current year] estimates.

[If ES vouchers present:]
Voucher amounts for [current year]:
  Q1 (04/15): $[amount]
  Q2 (06/15): $[amount]
  Q3 (09/15): $[amount]
  Q4 (01/15): $[amount]

Please confirm all estimated payments made and amounts paid.

------------------------------------------------------------

OTHER ITEMS
[Include if corresponding form was present:]

[If Form 1116:] - Foreign tax credit documentation
[If Form 4797:] - Any sales of business property?
[If Schedule C:] - Business income and expense summary
[If education credits:] - Form 1098-T for tuition paid
[If child care credit:] - Child/dependent care expenses
  and provider information
[If state returns:] - State-specific items for [state(s)]

------------------------------------------------------------

CHANGES & NEW ACTIVITY

Please let us know about any of the following in [current year]:
- Change in marital status
- Birth or adoption of a child
- Purchase or sale of a home
- New business started or closed
- Significant gifts made or received (over $18,000)
- Any other new income sources or life changes

============================================================
```

## Safety Constraints

- **Never include full SSNs in the output.** Taxpayer SSNs must be omitted entirely.
- **EINs for K-1 entities are included** — clients need these to match K-1s they receive.
- **Account identifiers use last 4 digits only** — do not include full account numbers.
- **Prior year amounts are reference only** — include in parentheses for context, not as expectations.
- **Omit sections with no activity** — if no rental property, skip the rental section entirely.
- **Always ask about unlisted items** — for every category, ask "do you have any accounts/entities/properties not listed above?"
