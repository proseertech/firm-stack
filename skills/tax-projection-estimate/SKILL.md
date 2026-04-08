---
name: tax-projection-estimate
version: 1.1.0
description: |
  Build a standardized tax projection estimate for a pass-through entity (Form 1065
  partnership or Form 1120S S-corporation). Ingests a trial balance from any GL system
  (QBO, Sage Intacct, Xero, NetSuite, or manual export), tags every account, and produces
  a formatted Excel workpaper with SUMIF-linked projections, prior-year comparison, and
  K-1 allocation by line item per partner/shareholder.
trigger: |
  "tax projection", "tax estimate", "K-1 estimate", "project the return",
  "estimate taxable income", "pass-through projection", "partnership projection",
  "S-corp projection"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# Tax Projection Estimate — Pass-Through Entities

## Purpose

Produce a standardized, auditable tax projection for a 1065 or 1120S entity. The deliverable is an Excel workpaper inserted into the client's financials workbook where every calculated cell is a formula and every income/expense line traces back to a tagged trial balance via SUMIF. The primary output is a K-1 allocation table broken out by line item per partner or shareholder.

## Required Inputs

- **Entity type**: Form 1065 (partnership) or Form 1120S (S-corporation)
- **Trial balance** — Excel or CSV export from any GL system (QBO, Sage Intacct, Xero, NetSuite, or manual). Must include account name and balance (debit/credit or net). Period should cover the full projection year.
- **General ledger** (when available) — Transaction-level detail for the same period. Used to investigate unusual TB balances, large variances, catch-all accounts, and reclassification items. If the GL is in the same workbook as the TB (common with QBO exports), use it directly. If separate, read it in.
- **Prior-year tax return** (PDF) — filed 1065 or 1120S with all schedules, K-1s, and depreciation reports
- **Owner/partner names and allocation percentages** — from the partnership agreement, S-corp shares, or prior-year K-1s
- **Special items** (if any): 1031 exchange HUDs, cost segregation study, guaranteed payment schedules, officer compensation analysis

## Workflow

### Phase 1: Ingest & Normalize Trial Balance

Read the trial balance regardless of source system. Normalize to a standard structure:
- Column A: Account name
- Column B: Debit
- Column C: Credit
- Column D: DR (CR) net amount

If the source is Sage Intacct, Xero, or NetSuite, the column layout may differ. Map to the standard structure. If the TB is missing debit/credit split (only has net), that's fine — use the net column as DR (CR).

**Validation gate**: TB must balance (total debits = total credits, or net = 0). If it doesn't, stop and flag.

### Phase 2: Tag Every Account

Add a "Tax Group" column to the trial balance sheet. Assign a tag to every single account. No account should be left untagged.

**Income tags** (credits on TB — negate with -SUMIF on projection):
`Gross Receipts`, `Sales Returns`, `Rental Income`, `Brokerage Income`,
`Interest Income`, `Other Income`, `Gain/Loss on Sale`, etc.

**COGS tags** (debits on TB):
`COGS` — all cost-of-goods-sold sub-accounts

**Expense tags** (debits on TB — SUMIF directly):
`Salaries & Wages`, `Officer Compensation`, `Commissions`,
`Repairs & Maintenance`, `Rents`, `Taxes & Licenses`, `Interest Expense`,
`Advertising`, `Insurance`, `HOA Expenses`, `Property Taxes`, `Utilities`,
`Professional Fees`, `Office Expenses`, `Dues & Subscriptions`,
`Employee Benefits`, `Pension/Retirement`, `Bad Debts`, `Depreciation`,
`Travel`, `Meals`, `Vehicle Expenses`, `Contract Labor`,
`Other Deductions`, etc.

**K-1 separately stated tags**:
`K1-Interest`, `K1-Dividends`, `K1-LTCG`, `K1-STCG`, `K1-1231`,
`K1-179`, `K1-Charitable`, `K1-TaxExempt`

**Nondeductible tags**:
`NONDEDUCTIBLE-Meals50` — 50% of meals (nondeductible portion)
`NONDEDUCTIBLE-Entertainment` — entertainment
`NONDEDUCTIBLE-Penalties` — government penalties and fines

**Reclassification tags**:
`CAPITAL-[description]` — capitalize to balance sheet (e.g., `CAPITAL-1108 Washington`)
`RECLASSIFY-[target]` — move to a different line

**Balance sheet tags** (tagged for completeness — ensures every account is accounted for):
`BS-Cash`, `BS-AR`, `BS-Inventory`, `BS-FixedAsset`, `BS-AccumDepr`,
`BS-OtherAsset`, `BS-AP`, `BS-Loans`, `BS-OtherLiab`, `BS-Equity`

Add Excel data validation (dropdown) to the tag column so tags are consistent.

**Tag column formatting** (optional but recommended): Apply conditional formatting or light color fills to the tag column by category for visual scanning:
- Income tags: light green fill
- Expense tags: light orange fill
- COGS tags: light blue fill
- BS tags: light gray fill
- K1 separately stated: light purple fill
- Nondeductible: light red fill
- Capital/reclassify: yellow fill

**Validation gate**: Run a check — `=SUMIF(E:E,"",D:D)` should equal zero. If any accounts are untagged, stop and resolve before proceeding.

### Phase 2b: Investigate Unusual Balances via General Ledger

Before tagging is final, scan the TB for accounts that need GL-level investigation. Drill into the general ledger for any account that meets these criteria:

- **Catch-all accounts**: "Ask my Accountant", "Uncategorized", "Other", "Suspense" — always investigate, regardless of balance size
- **Large year-over-year variance**: Any account where the balance changed > 50% vs prior year OR the absolute change exceeds $10,000
- **Wrong-sign balances**: Revenue accounts with debit balances, expense accounts with credit balances, assets with credit balances
- **Round-number balances**: Large round amounts (e.g., $50,000 exactly) may indicate estimates, reclassifications, or intercompany entries that need context
- **New accounts**: Any account that exists in the current TB but not the prior year — check what transactions created it
- **Aggregated "Other" categories**: "Other Deductions", "Other Income", "Miscellaneous" — if material, break out the GL transactions and consider splitting the tag

**GL investigation process:**
1. Filter or search the GL sheet for the account name
2. Read through the transactions — dates, payees, descriptions, amounts
3. Determine the correct tag (or split across multiple tags)
4. If the account needs reclassification (e.g., "Ask my Accountant" contains a property purchase), document the reclassification in the Supporting Detail sheet with recommended journal entries
5. Note findings in the projection's Notes section

The GL investigation often reveals the most important adjustments in the entire projection — property purchases booked as expenses, intercompany transfers miscoded as income, prior-year accruals hitting the current year, etc.

### Core Principle: Balance Sheet Accounts Are Cumulative — Always Use the Change

A trial balance shows ending balances. For every balance sheet account — fixed assets,
accumulated depreciation, intangible assets, accumulated amortization, equity, capital
contributions, distributions, retained earnings — the TB balance is the cumulative
total since inception, NOT the current-year activity.

**To determine what happened in the current year, always compute the change:**
```
Current-year activity = Current TB balance - Prior TB balance
```

If the workbook contains a prior-year TB sheet, reference it directly in formulas.
If only the prior-year return is available, use Schedule L ending balances.

This applies to every balance sheet analysis in the projection:

| Analysis | What to compare | Current-year activity tells you |
|----------|----------------|-------------------------------|
| Fixed assets | Current FA balance - Prior FA balance | Acquisitions (increase) or dispositions (decrease) |
| Accum depreciation | Current AccumDep - Prior AccumDep | Book depreciation recorded (if negative = dep added; if positive = dispositions removed dep) |
| Intangible assets | Current IA balance - Prior IA balance | New intangibles acquired or old ones disposed |
| Accum amortization | Current AccumAmort - Prior AccumAmort | Book amortization recorded (same logic as accum dep) |
| Contributions | Current contrib balance - Prior contrib balance | Cash/property contributed this year |
| Distributions | Current distrib balance - Prior distrib balance | Cash/property distributed this year |
| Retained earnings | Current RE - Prior RE | Prior-year net income that closed into RE |
| Loans | Current loan balance - Prior loan balance | New borrowings (increase) or repayments (decrease) |

**Never use a raw TB ending balance as a current-year income/expense figure.**
A $861,378 contributions balance means $861,378 total contributed since inception —
not $861,378 contributed this year.

### Phase 2c: Identify Book-Tax Differences (M-1 Adjustments)

Scan the TB and GL for common book-tax differences that will require adjustment on the projection. These flow through Schedule M-1 (or M-3) on the return and affect the gap between book income and taxable income.

**Common M-1 items to look for:**

Income timing differences:
- Advance payments / deferred revenue recognized on books but not yet taxable (or vice versa)
- Installment sale income — book may recognize full gain; tax may defer under §453
- Like-kind exchange gain deferred for tax but recognized on books
- Cancellation of debt income — may be excluded for tax under §108

Expense timing differences:
- Depreciation — book depreciation almost never matches tax (MACRS vs straight-line, bonus dep, §179). Always a difference.
- Amortization — book amort of intangibles vs §197 15-year amort for tax
- Bad debt expense — book may use allowance method; tax requires direct write-off (specific charge-off)
- Prepaid expenses — book may expense when paid; tax may require capitalization under 12-month rule
- Accrued expenses — related-party accruals not deductible until paid (§267)
- Inventory — §263A UNICAP adjustment (if applicable)
- Compensation accruals — bonuses accrued on books but not paid within 2.5 months of year-end

Permanent differences:
- 50% meals limitation (§274) — book deducts 100%, tax only 50%
- Entertainment — 100% nondeductible for tax (§274(a))
- Government fines and penalties — nondeductible for tax (§162(f))
- Life insurance premiums where entity is beneficiary — nondeductible
- Political contributions — nondeductible
- Tax-exempt interest income — on books but excluded from taxable income
- Officer life insurance proceeds — tax-exempt but on books

**Process**: For each M-1 item identified, determine whether it's already reflected in the TB (e.g., meals are already on the TB at 100% — need to add back 50% as nondeductible) or needs a separate adjustment line on the projection.

### Phase 2d: Analyze Fixed Asset and Intangible Asset Changes

Compare the current-year TB to the prior-year TB (or prior-year return Schedule L) for changes in fixed assets and intangibles. These changes reveal acquisitions, dispositions, and depreciation/amortization impacts.

**Fixed asset analysis:**

1. **Compare fixed asset account balances** — Compute `Current TB - Prior TB` for each asset account. If a prior-year TB sheet exists in the workbook, use formulas referencing both sheets:
   - Increase (positive change) = potential acquisition (drill into GL for purchase details)
   - Decrease (negative change) = potential disposition (drill into GL for sale/write-off)
   - No change = existing asset, continuing depreciation

2. **Compare accumulated depreciation** — Compute `Current TB - Prior TB`:
   - Change near zero = book depreciation hasn't been recorded (common — year-end AJE not yet posted). Flag this.
   - Change became more negative = depreciation was recorded normally
   - Change became less negative (increased toward zero) = dispositions removed accumulated dep

3. **Depreciation impact**:
   - Existing assets: Use the Future Depreciation Report from the prior-year return. This gives the exact tax depreciation for each asset in the projection year.
   - New acquisitions: Estimate depreciation based on asset class, placed-in-service date, cost basis, and applicable method (MACRS, §179, bonus). Flag for the preparer to confirm elections.
   - Dispositions: Stop depreciation as of the disposition date (mid-month for real property, half-year or mid-quarter for personal property). Calculate gain/loss on disposition (proceeds minus adjusted tax basis).

4. **§179 and bonus depreciation**: For new assets, evaluate whether §179 or bonus depreciation should be elected. Note: §179 is separately stated on K-1 (Line 12 / Box 11) — do NOT include it in ordinary income or rental income.

**Intangible asset analysis:**

1. **Compare intangible asset balances** — Compute `Current TB - Prior TB` for each intangible:
   - Positive change = new intangible acquired. Determine if §197 applies (15-year amortization)
   - Negative change = intangible disposed. Calculate remaining unamortized basis for loss recognition
   - No change = existing intangible, continuing amortization

2. **Compare accumulated amortization** — Compute `Current TB - Prior TB`:
   - Change near zero = book amort not yet recorded
   - Change became more negative = amortization recorded normally
   - Change became less negative = intangibles disposed (accum amort removed)

3. **Amortization impact**: Use the prior return's amortization schedules for existing intangibles. Estimate amortization on new intangibles based on acquisition date and applicable life.

**Output**: Document all asset changes in the Supporting Detail sheet. For each acquisition or disposition, note: asset description, date, cost/proceeds, tax basis, gain/loss, and depreciation/amortization impact on the projection.

### Phase 2e: Roll Forward Capital Accounts & Reconcile

Roll the ending capital from the prior-year return forward to the current-year beginning balance on the books. If they don't tie, quantify the gap — it means adjustments were posted to the books after the prior return was prepared.

**Process:**

1. **Extract prior-year ending capital** from the filed return:
   - Schedule M-2 ending balance (total partners' capital / shareholders' equity)
   - Per-partner/shareholder capital from K-1s (if available)
   - Schedule L ending equity section

2. **Extract current-year beginning capital** from the books:
   - Retained earnings on the current TB
   - Capital accounts on the current TB
   - Total equity section from the current TB

3. **Compute the rollforward:**
   ```
   Prior-year return ending capital (Schedule M-2)     $X,XXX,XXX
   + Current-year net income per books (TB)            $X,XXX,XXX
   + Contributions (TB)                                $X,XXX,XXX
   - Distributions (TB)                                ($X,XXX,XXX)
   = Expected current-year ending capital               $X,XXX,XXX

   Actual ending capital per current TB                 $X,XXX,XXX
   DIFFERENCE                                           $X,XXX
   ```

4. **If the difference is NOT zero:**
   - The gap represents post-filing adjustments to the prior year on the books — entries posted after the return was prepared (correcting entries, late invoices, reclass entries, etc.)
   - Quantify and document the difference
   - Drill into retained earnings / equity GL entries to identify what changed
   - Determine if the prior-year return should have been amended, or if the adjustment is correctly a current-year book item
   - Flag in the Notes section: "⚠ Prior-year capital rollforward difference of $X,XXX — see Supporting Detail"

5. **Document in Supporting Detail sheet:**
   - Prior return M-2 ending balance
   - Book beginning balance
   - Variance
   - List of post-filing entries causing the gap (from GL investigation)
   - Recommendation: amend prior year, adjust current year, or accept as immaterial

This check catches a common problem: the bookkeeper posts entries to a closed year after the return was filed, and the current year's books silently carry a different starting point than the return. If not caught, the M-2 rollforward on the current return won't tie and the preparer has to chase it during tax season.

### Phase 3: Read Prior-Year Return

Extract from the prior-year return PDF:
- Filed amounts for each form line (income, deductions, Schedule K items)
- Depreciation schedules and Future Depreciation Report (for existing asset dep estimates)
- K-1 allocation percentages (verify pro-rata or special allocations)
- Schedule L (balance sheet), M-1 (book-to-tax reconciliation), M-2 (capital account)
- Any Section 179 elections, 1031 exchanges, or other tax elections

These become the "Prior Year Actual" column on the projection.

### Phase 4: Build Projection with SUMIF Formulas

Create the "[Year] Tax Projection" sheet as the FIRST sheet in the workbook. Every income and expense line on the projection uses a SUMIF formula pulling from the tagged TB — never a hardcoded number.

**Column layout** (always this order):
| B: Description | C: [Prior Year] Actual | D: [Current Year] Estimated | E: Variance | F+: Notes |

- Column C: Hardcoded from the filed return (reference data)
- Column D: SUMIF formula referencing B{r} (the label cell in the same row) as the criteria — NEVER hardcode the tag name inside the formula. The column B label IS the tag. Form line references (e.g., "Line 1a") go in the Notes column, not in column B.
- Column E: Formula `=D{r}-C{r}`
- Notes column: Explanations, flags, assumptions

**Section order:**

1. **HEADER BLOCK** — Entity name, EIN, form type, tax year, basis, preparer, date, GL source

2. **INCOME** — Mapped to form lines. Use -SUMIF for income (credits are negative on TB).
   - 1065: Gross receipts (1a), Returns (1b), Net (1c), COGS (2), Gross profit (3), Other income (5), Total income (6)
   - 1120S: Same line structure
   - Rental entities: Rental income as primary line

3. **DEDUCTIONS / OPERATING EXPENSES** — Mapped to form lines. Use SUMIF directly (debits are positive).
   - 1120S: Officer comp (7), Salaries (8), Repairs (9), Bad debts (10), Taxes (12), Rents (13), Interest (14), Depreciation (14a), Advertising (16), Pension (17), Benefits (18), Other (20)
   - 1065: Same but no officer comp; rental entities list by expense category
   - TOTAL DEDUCTIONS subtotal (SUM formula)

4. **NET OPERATING INCOME** — Formula: Income minus Deductions
   - 1120S: Ordinary business income (Line 21)
   - 1065: Ordinary business income (Line 22) or Net rental RE income (Schedule K Line 2)

5. **TAX ADJUSTMENTS** (when applicable) — Depreciation detail, Section 179, cost seg impact, 1031 exchange, book-to-tax differences. Tax depreciation uses the Future Depreciation Report from the prior return for existing assets; new asset depreciation estimated separately.

6. **K-1 ALLOCATION BY LINE ITEM** — The primary deliverable.

   Columns: `K-1 Line | Description | [Curr Year] Total | [Owner 1] (XX%) | [Owner 2] (XX%) | ...`

   Total column = entity-level amount (Schedule K). Owner columns = formulas referencing Total (e.g., `=D{r}*0.5`). No prior year in this table — that comparison is in the sections above.

   **Use the correct form's line numbers:**

   FORM 1065 — SCHEDULE K-1 (Partner's Share):
   | Line | Description                           | Notes |
   |------|---------------------------------------|-------|
   | 1    | Ordinary business income (loss)       | Form 1065 line 22 |
   | 2    | Net rental real estate income (loss)  | Form 8825 net |
   | 3    | Other net rental income (loss)        | |
   | 4a   | Guaranteed payments — services        | Partner-specific; may not be pro-rata |
   | 4b   | Guaranteed payments — capital         | Partner-specific; may not be pro-rata |
   | 5    | Interest income                       | |
   | 6a   | Ordinary dividends                    | |
   | 7    | Royalties                             | |
   | 8    | Net short-term capital gain (loss)    | |
   | 9a   | Net long-term capital gain (loss)     | |
   | 10   | Net section 1231 gain (loss)          | |
   | 11   | Other income (loss)                   | |
   | 12   | Section 179 deduction                 | Separately stated — NOT in Line 1 or 2 |
   | 13   | Other deductions                      | |
   | 14a  | Net self-employment earnings          | General partners only |
   | 18a  | Tax-exempt interest income            | Informational — increases basis |
   | 18b  | Other tax-exempt income               | Informational — increases basis |
   | 18c  | Nondeductible expenses                | Informational — increases basis |
   | 19   | Distributions                         | Not taxable — reduces basis |
   | 20   | Other information (199A / QBI)        | Code Z |

   FORM 1120S — SCHEDULE K-1 (Shareholder's Share):
   | Box  | Description                           | Notes |
   |------|---------------------------------------|-------|
   | 1    | Ordinary business income (loss)       | Form 1120S line 21 |
   | 2    | Net rental real estate income (loss)  | Form 8825 net |
   | 3    | Other net rental income (loss)        | |
   | 4    | Interest income                       | Box 4, NOT Line 5 like 1065 |
   | 5a   | Ordinary dividends                    | Box 5a, NOT Line 6a like 1065 |
   | 6    | Royalties                             | Box 6, NOT Line 7 like 1065 |
   | 7    | Net short-term capital gain (loss)    | |
   | 8a   | Net long-term capital gain (loss)     | Box 8a, NOT Line 9a like 1065 |
   | 9    | Net section 1231 gain (loss)          | Box 9, NOT Line 10 like 1065 |
   | 10   | Other income (loss)                   | |
   | 11   | Section 179 deduction                 | Separately stated — NOT in Box 1 |
   | 12   | Other deductions                      | Incl charitable contributions (12a) |
   | 13   | Credits                               | |
   | 16a  | Tax-exempt interest income            | Informational — increases basis |
   | 16b  | Other tax-exempt income               | Informational — increases basis |
   | 16c  | Nondeductible expenses                | Informational — increases basis |
   | 16d  | Distributions                         | Box 16d, NOT Line 19 like 1065 |
   | 17   | Other information (199A / QBI)        | Code V |

   **KEY LINE NUMBER DIFFERENCES (1065 vs 1120S):**
   - Interest: 1065 Line 5 vs 1120S Box 4
   - Dividends: 1065 Line 6a vs 1120S Box 5a
   - LTCG: 1065 Line 9a vs 1120S Box 8a
   - Sec 1231: 1065 Line 10 vs 1120S Box 9
   - Distributions: 1065 Line 19 vs 1120S Box 16d
   - 1065 has guaranteed payments (4a/4b) and SE earnings (14a) — no 1120S equivalent
   - 1120S has credits (Box 13) — different treatment on 1065

   Required bottom rows:
   - **Est. Taxable K-1 Income**: SUM of taxable lines (excl distributions, nondeductible, tax-exempt). Formula in each owner column.
   - **Nondeductible detail**: 50% meals, entertainment, penalties — subtotal with per-owner formulas.
   - **Distributions**: Always shown. Per-owner amounts from TB (may differ by owner).

7. **199A / QBI ESTIMATE** (if applicable) — QBI, 20% of QBI, W-2 limitation, estimated deduction per owner. Note: final calc on personal return.

8. **EQUITY / CAPITAL ROLLFORWARD** — Always include. Grid format: rows are categories, columns are owners + total.

   Columns: `Description | [Owner 1] | [Owner 2] | Total | Notes`

   ```
   EQUITY / CAPITAL ROLLFORWARD
                                 Dan Berger    Kobi Ben      Total         Notes
   Prior-year ending capital     [formula]     [formula]     [formula]     From prior TB or M-2
   
   Current-year changes:
     Contributions               [formula]     [formula]     =sum
     Distributions               [formula]     [formula]     =sum
     Capital account changes     [formula]     [formula]     =sum
     Retained earnings changes   n/a           n/a           [formula]     Entity-level only
   Total changes                 =SUM          =SUM          =SUM
   
   Expected ending capital       =prior+chg    =prior+chg    =sum
   Actual ending per TB          [formula]     [formula]     =sum
   DIFFERENCE                    =exp-act      =exp-act      =sum          ⚠ if ≠ $0
   ```

   **Critical: Use CHANGES, not raw TB balances.** Every equity line computes
   `Current TB balance - Prior TB balance` using SUMIF against both TB sheets.
   A contributions balance of $861,378 is cumulative since inception — the CHANGE
   might be $0 if nothing was contributed this year.

   If difference ≠ $0, flag with ⚠ — means post-filing adjustments were posted
   to the prior year on the books after the return was filed.

9. **NOTES & ASSUMPTIONS** — Numbered. Flag open items with ⚠. Always include: basis method, GL source, depreciation source, assumed amounts, items not yet in books, passive activity / REP status for rental entities.

10. **RECONCILIATION CHECK** — Verify every TB dollar is accounted for:
   ```
   Total income tags (negated)     = -SUMIFS(...)
   Total expense tags              =  SUMIFS(...)
   Total COGS tags                 =  SUMIFS(...)
   Total capital/reclassify tags   =  SUMIFS(...)
   Total BS tags                   =  SUMIFS(...)
   Total nondeductible tags        =  SUMIFS(...)
   TB Grand Total                  =  [from TB]
   DIFFERENCE (should be $0)       =  [formula]
   ```

11. **DISCLAIMER** — "Preliminary estimate based on unaudited [GL source] data and [prior year] filed return. Actual K-1 amounts will vary based on final adjustments."

### Phase 5: Supporting Detail (when needed)

Add a second sheet for:
- GL detail on flagged items (large, unusual, or reclassified transactions)
- Recommended journal entries (account, debit, credit, memo)
- 1031 exchange basis calculations
- Cost segregation impact analysis
- "Ask my Accountant" or other catch-all account clearing detail

### Phase 6: Verify & Deliver

Spot-check:
1. Change one expense input on the TB → confirm it cascades through SUMIF → total → net income → K-1 allocation
2. Reconciliation check = $0
3. No untagged accounts
4. K-1 allocation total ties to net income sections above
5. No circular references

## Control Points

Human must confirm before proceeding past these gates:

- **Tag review** — After Phase 2, present the full tag mapping and ask the user to confirm before building the projection. Especially: reclassification tags (CAPITAL, RECLASSIFY), items tagged NONDEDUCTIBLE, and any catch-all accounts ("Ask my Accountant", "Uncategorized").
- **Special item treatment** — Before applying 1031 exchange, cost seg, or other tax elections, confirm the approach with the user (e.g., "Slip 54 gain deferred via 1031 — correct?").
- **Depreciation estimates** — Tax depreciation is pulled from the prior return's Future Dep Report, not from GL books. Confirm with user if new assets require depreciation estimates beyond what the prior return provides.
- **Owner percentages** — Confirm allocation percentages from the partnership agreement or S-corp shares, especially if any special allocations exist (guaranteed payments, preferred returns, waterfall provisions).

## Red Flags

Pause and surface to the user immediately if:

- TB doesn't balance (debits ≠ credits)
- "Ask my Accountant" or "Uncategorized" account has a balance > $0
- Depreciation on the GL differs from the prior return's depreciation schedules by more than 10% (likely stale book depreciation)
- Property tax, rent, or payroll variance > 30% year-over-year without explanation
- Intercompany balances (due-to/due-from) are mismatched across related entities
- Distributions exceed estimated income (potential basis issue)
- Any account balance that is the wrong sign (e.g., revenue with a debit balance, asset with a credit balance) — may indicate a reclassification need
- Negative retained earnings on the prior return combined with current-year losses (basis limitation risk)

## Output Format

**Sheet 1**: "[Year] Tax Projection" — first sheet in the workbook. SUMIF-linked to tagged TB. K-1 allocation by line item with per-owner columns.

**Sheet 2**: "Supporting Detail" (when needed) — GL detail, journal entries, 1031 calculations, cost seg analysis.

**Tagged TB**: The original trial balance sheet with the Tax Group column added (non-destructive — original data preserved).

## Excel Formula Rules

Every calculated cell must use a formula. Never hardcode a derived value.

| Cell Type | Formula Pattern |
|-----------|----------------|
| Income line (curr year) | `=-SUMIF('TB Sheet'!$E:$E,B{r},'TB Sheet'!$D:$D)` — B{r} is the label cell |
| Expense line (curr year) | `=SUMIF('TB Sheet'!$E:$E,B{r},'TB Sheet'!$D:$D)` — B{r} is the label cell |
| Variance | `=D{r}-C{r}` |
| Section total | `=SUM(D{start}:D{end})` |
| Net income | `=D{income}-D{expenses}-D{depreciation}` |
| K-1 per-owner | `=D{r}*0.5` (or actual %) |
| K-1 taxable total | `=SUM(D{line_refs})` |
| 199A deduction | `=MIN(D{qbi}*0.2, D{w2}*0.5)` |
| Reconciliation | `=SUM(all_tag_totals) - TB_grand_total` |

**What stays hardcoded** (inputs only): prior-year return amounts, owner percentages, tax rates, depreciation from future dep reports, property names, notes text.

Track row numbers in a `rows = {}` dict while building so formulas reference correct cells.

## Styling Rules

**Only 5 fill colors. Data rows have NO fill — leave them white.**
Fills are reserved for structural rows only. This keeps the workpaper light and readable.

| Element | Fill | Font | Border |
|---------|------|------|--------|
| Section headers | #1F4E79 (dark blue) | White, bold, 11pt | — |
| Column headers | #D6E4F0 (soft blue) | Bold, 10pt | — |
| Total rows | #E2EFDA (soft green) | Bold | top=medium, bottom=double |
| Subtotal rows | #F2F2F2 (light gray) | Bold | bottom=thin |
| Flagged items | #FFF2CC (soft yellow) | Bold | — |
| **Data rows** | **No fill (white)** | Normal, 10pt | — |
| Losses / negatives | No fill | Red font (#C00000) | — |
| Notes column | No fill | Gray italic (#666666), 9pt | — |
| Non-taxable K-1 items | No fill | Gray font (#666666) | — |

Numbers: Right-aligned, `#,##0` or `#,##0;(#,##0)` for items that can be negative.
Column widths: B=44, C-F=15-17, Notes=45.

**Trial Balance tag column fills** (optional — for visual scanning):

| Tag Category | Fill Color |
|-------------|-----------|
| Income tags | #E2EFDA (light green) |
| Expense tags | #FDE9D9 (light orange) |
| COGS tags | #D6E4F0 (light blue) |
| BS tags | #F2F2F2 (light gray) |
| K1 separately stated | #E8D5F5 (light purple) |
| Nondeductible | #FFC7CE (light red) |
| Capital/reclassify | #FFF2CC (light yellow) |

## Safety Constraints

- This is an ESTIMATE, not a filed return. Always include the disclaimer.
- Do not present the projection as final or filed without explicit CPA review.
- Do not post journal entries to the GL without human approval — recommend only.
- Do not modify the original trial balance data — only add the Tax Group tag column.
- Do not assume owner allocation percentages — verify from K-1s or partnership agreement.
- Flag but do not resolve ambiguous tax positions (1031 qualification, 179 eligibility, passive activity status) — those require CPA judgment.

## Pitfalls & Implementation Notes

### PDF Extraction
- Use `pymupdf` (preferred) or `pdfplumber` for tax return PDFs. Both handle multi-page text-based returns well. Some HUD/closing statement PDFs are scanned images and will extract as empty — fall back to GL entries or ask the user.
- **PDF column misalignment**: Tax return PDFs often merge columns when extracted to text. The "Section 179 deduction" amount can appear to be "Other income" or vice versa. Always verify by checking if the total reconciles (e.g., rental income + LTCG - 179 = net income per analysis).
- The Section 199A Information Worksheet is especially tricky — columns for QBI, W-2 wages, and UBIA of qualified property often merge. Cross-reference totals (entity-level should be 2x per-shareholder amounts for 50/50 splits).

### Entity-Specific Traps
- **S-Corp charitable contributions go to K-1, NOT page 1**: Unlike C-corps, S-Corp charitable contributions are NOT deducted on page 1 of Form 1120S. They flow through K-1 Box 12A and are deducted on the shareholder's personal return. Don't double-count.
- **S-Corp COGS for dealer businesses**: For inventory businesses (boats, cars, etc.), COGS uses Form 1125-A (beginning inventory + purchases + labor - ending inventory). QBO may show COGS as sub-accounts (Finished Goods, Freight, Parts, Labor, Commissions) that sum to approximately the same number but may differ due to inventory timing. For a projection, use the TB sub-account totals directly.
- **Reasonable compensation**: For S-Corps, verify officer W-2 amounts. Check prior-year Form 1125-E for the officer compensation breakdown. QBO often lumps officer comp into general "Salaries & wages."
- **SSTB status**: Check the prior-year 199A Information Worksheet for the Specified Service Trade or Business flag. This affects the 199A deduction phase-out.
- **Settlement dates determine tax year**: A January closing is NEXT year's taxable event even if the property was under contract in December. Check HUD settlement dates carefully.

### Asset-Specific Traps
- **Water/boat slips are non-depreciable**: Marina slips, dock spaces, and water rights are treated like land — no depreciation. Only closing costs (amortizable) and structural improvements generate deductions.
- **Accumulated amortization can decrease**: When an amortizable asset is sold, its accumulated amortization is removed from the books. If accum amort goes DOWN year-over-year, check for asset dispositions — don't assume it's an error.
- **Escrow accounts**: Large escrow balances often relate to 1031 exchanges or pending closings. Investigate rather than ignore.
- **HUD "Borrower" vs "Buyer"**: When an entity buys through a 1031 QI, it appears as "Borrower" on the ALTA settlement statement even if there's no loan — "Borrower" just means buyer in ALTA format.

### Balance Sheet & Intercompany
- **Intercompany receivables/payables**: Changes in "Due from/to" accounts are balance sheet movements, not income. Don't include in the income calculation.
- **Two-year comparison worksheet**: Many tax return PDFs include this (usually near the end). It's a quick way to verify prior-year amounts and spot year-over-year changes without reading every schedule.

### Technical / Environment
- Use `openpyxl` for Excel manipulation. On Ubuntu, install with `pip install --break-system-packages openpyxl pdfplumber`.
- The `execute_code` sandbox may not see user-installed packages. Use `mcp_terminal` with `export HOME=/home/[user]` for openpyxl/pdfplumber work.
- When building formulas in openpyxl, single quotes in sheet name references must be escaped: `'Trial Balance 2025'!$E:$E`

### Consistency Across Workbooks
- When building projections for multiple entities in the same client group, verify the output is visually identical: same 5-color palette, same section order, same column layout, same K-1 table structure. Side-by-side comparison catches drift.
- If delegating workbook builds to subagents, specify exact hex color codes and explicitly state "data rows = NO fill." Subagents tend to over-apply fills (coloring every data row with light blue) and use bolder/darker color variants unless constrained.
- The firm-stack repo at `proseertech/firm-stack` is the canonical source for the skill. Keep Hermes local copy and firm-stack repo in sync after updates.
