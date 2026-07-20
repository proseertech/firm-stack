# Pitfalls & Implementation Notes

Worked traps and environment notes gathered from real projection builds. Skim before starting;
consult the relevant section when you hit the situation (a scanned HUD, an S-corp with
charitable contributions, stale book depreciation, a multi-entity client group).

---

## PDF Extraction
- Use `pymupdf` (preferred) or `pdfplumber` for tax return PDFs. Both handle multi-page text-based returns well. Some HUD/closing statement PDFs are scanned images and will extract as empty — fall back to GL entries or ask the user.
- **PDF column misalignment**: Tax return PDFs often merge columns when extracted to text. The "Section 179 deduction" amount can appear to be "Other income" or vice versa. Always verify by checking if the total reconciles (e.g., rental income + LTCG - 179 = net income per analysis).
- The Section 199A Information Worksheet is especially tricky — columns for QBI, W-2 wages, and UBIA of qualified property often merge. Cross-reference totals (entity-level should be 2x per-shareholder amounts for 50/50 splits).

## Entity-Specific Traps
- **S-Corp charitable contributions go to K-1, NOT page 1**: Unlike C-corps, S-Corp charitable contributions are NOT deducted on page 1 of Form 1120S. They flow through K-1 Box 12A and are deducted on the shareholder's personal return. Don't double-count.
- **S-Corp COGS for dealer businesses**: For inventory businesses (boats, cars, etc.), COGS uses Form 1125-A (beginning inventory + purchases + labor - ending inventory). QBO may show COGS as sub-accounts (Finished Goods, Freight, Parts, Labor, Commissions) that sum to approximately the same number but may differ due to inventory timing. For a projection, use the TB sub-account totals directly.
- **Reasonable compensation**: For S-Corps, verify officer W-2 amounts. Check prior-year Form 1125-E for the officer compensation breakdown. QBO often lumps officer comp into general "Salaries & wages."
- **SSTB status**: Check the prior-year 199A Information Worksheet for the Specified Service Trade or Business flag. This affects the 199A deduction phase-out.
- **Settlement dates determine tax year**: A January closing is NEXT year's taxable event even if the property was under contract in December. Check HUD settlement dates carefully.

## Asset-Specific Traps
- **Water/boat slips are non-depreciable**: Marina slips, dock spaces, and water rights are treated like land — no depreciation. Only closing costs (amortizable) and structural improvements generate deductions.
- **Accumulated amortization can decrease**: When an amortizable asset is sold, its accumulated amortization is removed from the books. If accum amort goes DOWN year-over-year, check for asset dispositions — don't assume it's an error.
- **Escrow accounts**: Large escrow balances often relate to 1031 exchanges or pending closings. Investigate rather than ignore.
- **HUD "Borrower" vs "Buyer"**: When an entity buys through a 1031 QI, it appears as "Borrower" on the ALTA settlement statement even if there's no loan — "Borrower" just means buyer in ALTA format.

## Balance Sheet & Intercompany
- **Intercompany receivables/payables**: Changes in "Due from/to" accounts are balance sheet movements, not income. Don't include in the income calculation.
- **Two-year comparison worksheet**: Many tax return PDFs include this (usually near the end). It's a quick way to verify prior-year amounts and spot year-over-year changes without reading every schedule.

## Technical / Environment
- Use `openpyxl` for Excel manipulation. On Ubuntu, install with `pip install --break-system-packages openpyxl pdfplumber`.
- The `execute_code` sandbox may not see user-installed packages. Use `mcp_terminal` with `export HOME=/home/[user]` for openpyxl/pdfplumber work.
- When building formulas in openpyxl, single quotes in sheet name references must be escaped: `'Trial Balance 2025'!$E:$E`

## Consistency Across Workbooks
- When building projections for multiple entities in the same client group, verify the output is visually identical: same 5-color palette, same section order, same column layout, same K-1 table structure. Side-by-side comparison catches drift.
- If delegating workbook builds to subagents, specify exact hex color codes and explicitly state "data rows = NO fill." Subagents tend to over-apply fills (coloring every data row with light blue) and use bolder/darker color variants unless constrained.
- The firm-stack repo at `proseertech/firm-stack` is the canonical source for the skill. Keep Hermes local copy and firm-stack repo in sync after updates.
