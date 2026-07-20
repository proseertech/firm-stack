---
name: tax-projection-estimate
version: 1.4.0
description: |
  Build a standardized, auditable tax projection for a pass-through entity (Form 1065
  partnership or Form 1120S S-corporation) from a GL trial balance plus the prior-year
  return. Tags every TB account, links every line with SUMIF formulas, compares to prior
  year, and produces a K-1 allocation broken out by line item per partner/shareholder — the
  primary deliverable. Use this whenever someone wants to know where a partnership or S-corp
  will land for the year or what the owners' K-1s will look like: "run a tax projection",
  "estimate taxable income for [entity]", "what will the K-1s be", "project the partnership
  return", "give the partners a Q3 estimate", "build a K-1 estimate from the trial balance".
  Ingests a TB from any GL (QBO, Sage Intacct, Xero, NetSuite, or a manual export). For
  pass-throughs only — not 1040, 1120 (C-corp), 1041, or 990.
trigger: |
  "tax projection", "tax estimate", "K-1 estimate", "project the return",
  "project the K-1s", "what will the K-1s look like", "estimate taxable income",
  "estimate the partners' income", "pass-through projection", "partnership projection",
  "S-corp projection", "projection from the trial balance", "quarterly estimate for the partnership",
  "give the owners an estimate"
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

This is an estimate for planning, not a filed return — its value is that it is directionally right and fully traceable, so the preparer can see exactly where every number came from during tax season.

## Required Inputs

- **Entity type**: Form 1065 (partnership) or Form 1120S (S-corporation)
- **Trial balance** — Excel or CSV export from any GL system (QBO, Sage Intacct, Xero, NetSuite, or manual). Must include account name and balance (debit/credit or net). Period should cover the full projection year.
- **General ledger** (when available) — Transaction-level detail for the same period. Used to investigate unusual TB balances, large variances, catch-all accounts, and reclassification items. If the GL is in the same workbook as the TB (common with QBO exports), use it directly. If separate, read it in.
- **Prior-year tax return** (PDF) — filed 1065 or 1120S with all schedules, K-1s, and depreciation reports
- **Owner/partner names and allocation percentages** — from the partnership agreement, S-corp shares, or prior-year K-1s
- **Special items** (if any): 1031 exchange HUDs, cost segregation study, guaranteed payment schedules, officer compensation analysis

If a required input is missing, ask before building — a projection built on a missing return or the wrong ownership split reads as authoritative but is wrong, and the error surfaces only when the real K-1s don't match.

## Workflow

### Phase 1: Ingest & Normalize Trial Balance

Read the trial balance regardless of source system. Normalize to a standard structure:
- Column A: Account name
- Column B: Debit
- Column C: Credit
- Column D: DR (CR) net amount

If the source is Sage Intacct, Xero, or NetSuite, the column layout may differ. Map to the standard structure. If the TB is missing debit/credit split (only has net), that's fine — use the net column as DR (CR).

**Validation gate**: TB must balance (total debits = total credits, or net = 0). If it doesn't, stop and flag — an unbalanced TB means the projection is built on incomplete data.

### Phase 2: Tag Every Account

Add a "Tax Group" column to the trial balance sheet and assign a tag to every single account. No account should be left untagged — an untagged account is silently dropped from the projection, understating income or deductions.

The full tag category map (income, COGS, expense, K-1 separately stated, nondeductible, reclassification, and balance-sheet tags) is in **`references/account-tagging.md`** — read it while tagging. Add Excel data validation (dropdown) to the tag column so tags are consistent, and optionally color the tag column by category for visual scanning (colors in the same reference).

**Validation gate**: Run a check — `=SUMIF(E:E,"",D:D)` should equal zero. If any accounts are untagged, stop and resolve before proceeding.

### Phase 2b: Investigate Unusual Balances via General Ledger

Before tagging is final, scan the TB for accounts that need GL-level investigation. Drill into the general ledger for any account that meets these criteria:

- **Catch-all accounts**: "Ask my Accountant", "Uncategorized", "Other", "Suspense" — since this is an estimate (directionally correct, not perfect), investigate only when the balance is large enough that misclassification could meaningfully shift the projection. For small balances in catch-all accounts, note their existence in the projection Notes so the preparer can resolve them during the actual return — do not drill into the GL for the estimate.
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

Identify book-tax differences that actually apply to this client based on evidence in the TB, GL, and prior-year return. The common M-1 items are catalogued in **`references/account-tagging.md`** — use that list to prompt yourself to check whether each category appears in the current-year TB, not as a checklist of adjustments to manufacture. Only document an adjustment when the underlying account or transaction exists; skip categories that don't apply to this client.

For each M-1 item identified, determine whether it's already reflected in the TB (e.g., meals are already on the TB at 100% — need to add back 50% as nondeductible) or needs a separate adjustment line on the projection.

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

These become the "Prior Year Actual" column on the projection. (For PDF extraction gotchas — merged columns, scanned HUDs, the 199A worksheet — see `references/pitfalls.md`.)

### Phase 4: Build Projection with SUMIF Formulas

Create the "[Year] Tax Projection" sheet as the FIRST sheet in the workbook. Every income and expense line on the projection uses a SUMIF formula pulling from the tagged TB — never a hardcoded number, so a change to any TB balance cascades through the whole projection.

Exact formula patterns, the column layout, styling palette, and column widths are in **`references/workbook-build.md`** — follow it while building.

**Helper (recommended)**: `scripts/build_projection.py` (openpyxl) builds the SUMIF-wired, styled skeleton for you — it holds the exact palette/font/format/width constants, writes the tagged-TB sheet with the tag column colored by category, wires income/expense lines as real `=SUMIF(...)` formulas referencing the TB tag column (never hard-coded sums or tags), and builds the per-owner K-1 grid. It also enforces the documented failure mode — **data rows get NO fill** (only header/total/subtotal/section/flagged rows are filled), verified by `audit_no_data_fill()`. Import it as a module, or run `python scripts/build_projection.py --demo` to see a 2-shareholder 1120S example (writes to a temp path). Use it to avoid re-deriving the styling by hand.

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

   **Use the correct form's line numbers.** The full 1065 and 1120S K-1 line maps and the key line-number differences between them are in **`references/k1-line-map.md`** — the two forms number the same items differently (e.g., interest is 1065 Line 5 vs 1120S Box 4), and using the wrong set is a silent error.

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

## Safety Constraints

- This is an ESTIMATE, not a filed return. Always include the disclaimer.
- Do not present the projection as final or filed without explicit CPA review.
- Do not post journal entries to the GL without human approval — recommend only.
- Do not modify the original trial balance data — only add the Tax Group tag column.
- Do not assume owner allocation percentages — verify from K-1s or partnership agreement.
- Flag but do not resolve ambiguous tax positions (1031 qualification, 179 eligibility, passive activity status) — those require CPA judgment.

## References

- **`references/account-tagging.md`** — tag category map + book-tax (M-1) difference list (Phases 2 and 2c)
- **`references/k1-line-map.md`** — Form 1065 vs 1120S K-1 line numbers and key differences (Phase 4, section 6)
- **`references/workbook-build.md`** — Excel formula patterns, column layout, styling palette, column widths (Phase 4)
- **`references/pitfalls.md`** — PDF extraction, entity/asset-specific traps, environment setup, and multi-entity consistency notes
- **`scripts/build_projection.py`** — openpyxl helper that builds the SUMIF-wired, styled skeleton (tagged-TB + projection + per-owner K-1 grid) and enforces the no-fill-on-data-rows rule (Phase 4; `--demo` for a runnable 1120S example)
