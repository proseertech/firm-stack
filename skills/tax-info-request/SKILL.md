---
name: tax-info-request
version: 2.0.0
description: |
  Review a prior year individual tax return (Form 1040) PDF and generate a
  flat, one-line-per-item information request for the current tax year.
  Extracts every income source, deduction, entity, and account from the
  return, then produces a checklist-style document request with prior year
  reference amounts — one request per line, ready to paste into a portal
  or tracker.
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

Generate a complete information request for the upcoming tax year by extracting every relevant item from the prior year Form 1040. The output is a **flat checklist** — one request per line, no section headers, no sub-bullets — ready to paste line-by-line into a portal, tracker, or email. Prior year amounts appear in parentheses for context.

## Required Inputs

- Path to the prior year tax return PDF

## Optional Inputs

- **Meeting notes / intake context** — Notes from client calls, planning meetings, or advisory discussions. Examples: "client sold ~$1.9M in stock", "bought a home in 2025", "considering angel investments". The skill weaves these into the request as specific line items.
- **Already-collected items** — List of documents or info already obtained. Examples: "already have spouse email", "W-2s received". These items are excluded from the output.
- **Override notes** — e.g., "skip rental section", "add crypto question", "they sold the property", "new baby born in 2025"

**Prompt for these if not provided.** Ask:
> Do you have any meeting notes, intake call context, or known life events for this client? Also let me know if you've already collected any documents so I can exclude them.

## Current Tax Year Thresholds (2025)

Always use the **current filing year** amounts, not the prior year's. Key thresholds:
- Gift tax annual exclusion: **$19,000** (2025)
- Standard deduction (MFJ): **$30,000** (2025)
- Standard deduction (Single): **$15,000** (2025)
- FBAR threshold: $10,000 aggregate (static)
- Form 8938 thresholds: $50,000/$75,000/$200,000/$400,000 (static, varies by filing status and residence)

Update these amounts if the current date indicates a different filing year.

## Workflow

1. **Read the full return** — Read the tax return PDF in batches of 20 pages. Read ALL pages — K-1 details, state returns, and supporting statements are often at the end. Do not stop early.

2. **Extract data** — Systematically extract data from every section of the return:

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

   **J. Foreign Entity / Closely Held Company Detection**
   - Form 8938 (FATCA): Any specified foreign financial assets, including ownership in foreign entities
   - Form 5471 (controlled foreign corporation), Form 8865 (foreign partnership), or any foreign entity reporting
   - FBAR signature authority over foreign accounts
   - If detected: flag for expanded questioning (see Closely Held / Foreign Entity Rules below)

3. **Apply meeting notes & context** — If the user provided meeting notes or intake context:
   - Convert known facts into specific request lines (e.g., "client sold stock" → request sale docs, cost basis, broker statement)
   - Add advisory-driven questions (e.g., estate plan discussion → flag estate plan status)
   - Incorporate life events as targeted requests (e.g., "bought a home" → Form 1098, property tax statement)

4. **Remove already-collected items** — If the user specified items already obtained, exclude them from the output entirely.

5. **Apply user overrides** — If the user provided override notes:
   - "Skip [section]" — omit those items from the output
   - "Add [topic]" — add a custom request line
   - "They sold [property]" — replace rental/property lines with sale-related requests (1099-S, closing statement, depreciation recapture)
   - "New [life event]" — add relevant request lines

6. **Generate the information request** — Produce the output using the format rules below.

## Closely Held / Foreign Entity Rules

When the return shows ownership in a closely held company — especially a foreign entity (Form 8938, Form 5471, FBAR signature authority) — and meeting notes or the return indicate a partial sale or ongoing ownership, generate these additional lines:

```
Sale documentation for [Entity] shares — date, number of shares, proceeds, cost basis, selling expenses
[Entity] — remaining shares held as of 12/31/[current year] and year-end fair market value
[Entity] — maximum value of shares held at any point during [current year] (needed for Form 8938)
[Entity] — any additional acquisitions or dispositions of shares in [current year] beyond known sale
[Entity] — any dividends or distributions received in [current year]
```

Adjust language if the entity is a partnership interest rather than shares.

## Control Points

- **Sensitive client data** — The output will contain client names, addresses, EINs, and account fragments. Confirm the output destination (file path, email draft, etc.) before writing.
- **Missing pages** — If the PDF appears incomplete (e.g., no page 2 of Form 1040, or K-1s referenced but not included), flag what appears to be missing before generating the request.

## Red Flags

- Return references K-1 entities but no K-1s are included in the PDF — note which entities are expected
- Foreign accounts question answered Yes but no FBAR/FATCA details visible — flag for follow-up
- Large estimated tax payments that may indicate underwithholding pattern — include in the request
- Digital assets question answered Yes but no Schedule D/Form 8949 crypto activity — ask about current year activity
- Foreign entity ownership detected but no Form 5471/8865 included — flag for review

## Output Format

**Flat checklist. One request per line. No section headers, no grouping, no sub-bullets, no decorative formatting.**

Rules:
- Each line is a standalone request that can be copied independently into a portal or tracker
- Lead with the document name or topic, not "Please provide..."
- Include prior year amounts in parentheses for context — keep brief
- Use short, direct phrasing — checklist style, not letter style
- No "Dear Client", no greeting, no closing, no signature blocks
- No dashes/equals separators between sections
- Group related items together in the list order, but do not add headers

### Example Output

```
Confirm current home address: [address from prior year return]
Confirm filing status for 2025: Married Filing Jointly
Confirm dependents still claimed: [Name] (son), [Name] (daughter) — any new dependents?
2025 W-2 — Dialog Enterprises Inc. (2024: $116,748)
2025 W-2 — Salisbury House Management LLC (2024: $89,104)
Any new employers or job changes in 2025?
2025 Form 1099 composite — Charles Schwab acct ending 4821
2025 Form 1099 composite — Robinhood Securities acct ending 7733
Any brokerage/investment accounts not listed above?
2025 Form 1099-INT — TD Bank acct ending 0092 (2024 interest: $1,204)
Any new bank accounts earning interest?
2025 Form 1099-R for any IRA/Roth/retirement distributions (2024: $7,810 Roth conversion via Robinhood)
2025 Schedule K-1 — ABC Partners LP (EIN: 12-3456789)
2025 Schedule K-1 — XYZ Holdings LLC (EIN: 98-7654321)
Any new K-1 entities, or any entities you are no longer involved in?
Sale documentation for Dialog Enterprises shares — date, shares sold, proceeds, cost basis, expenses
Dialog Enterprises — remaining shares held as of 12/31/2025 and year-end fair market value
Dialog Enterprises — maximum value of shares during 2025 (for Form 8938)
Dialog Enterprises — any additional share transactions in 2025 beyond the known sale
Dialog Enterprises — any dividends or distributions received in 2025
2025 Form 1098 — mortgage interest statement (2024: $18,500)
2025 property tax bills/statements (2024: $12,300)
Charitable contribution receipts — cash and non-cash (2024 cash: $8,200)
Summary of unreimbursed medical/dental expenses paid in 2025 (2024: $4,100)
Foreign bank accounts — highest balance during 2025 for each account (FBAR required if aggregate > $10,000)
Foreign bank accounts — interest earned in 2025 from each account
Any new foreign bank or financial accounts opened in 2025?
Confirm all estimated tax payments made in 2025 and amounts (2024 total: $24,000; $6,400 overpayment applied)
2025 Form 1098-T for tuition paid
Dependent care expenses and provider info for 2025
Any cryptocurrency or digital asset transactions in 2025?
Any purchase or sale of a home in 2025?
Any change in marital status in 2025?
Any births, adoptions, or new dependents in 2025?
Any new business started or closed in 2025?
Any gifts made over $19,000 to a single person in 2025?
Any other new income sources or significant life changes in 2025?
```

## Safety Constraints

- **Never include full SSNs in the output.** Taxpayer SSNs must be omitted entirely.
- **EINs for K-1 entities are included** — clients need these to match K-1s they receive.
- **Account identifiers use last 4 digits only** — do not include full account numbers.
- **Prior year amounts are reference only** — include in parentheses for context, not as expectations.
- **Omit lines with no activity** — if no rental property, skip rental lines entirely.
- **For every category, include an "any not listed?" catch-all line.**
- **Use current-year thresholds** — never use prior year amounts for exclusion limits, gift limits, etc.
