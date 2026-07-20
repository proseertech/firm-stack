# Account Tagging & Book-Tax (M-1) Differences

Reference for Phase 2 (tag every account) and Phase 2c (identify M-1 adjustments). The
workflow, validation gates, and judgment live in SKILL.md — this file is the category maps.

---

## Tag categories

Add a "Tax Group" column to the trial balance sheet and assign a tag to every single
account. No account should be left untagged.

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

**Tag column formatting** (optional but recommended): Apply conditional formatting or light
color fills to the tag column by category for visual scanning:
- Income tags: light green fill
- Expense tags: light orange fill
- COGS tags: light blue fill
- BS tags: light gray fill
- K1 separately stated: light purple fill
- Nondeductible: light red fill
- Capital/reclassify: yellow fill

(Exact hex codes for the tag-column fills are in `references/workbook-build.md`.)

---

## Book-tax differences (M-1 items) to check against the TB

Identify book-tax differences that actually apply to this client based on evidence in the
TB, GL, and prior-year return. This list is a prompt to check whether each category appears
in the current-year TB — not a checklist of adjustments to manufacture. Only document an
adjustment when the underlying account or transaction exists; skip categories that don't
apply to this client.

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

**Process**: For each M-1 item identified, determine whether it's already reflected in the TB
(e.g., meals are already on the TB at 100% — need to add back 50% as nondeductible) or needs a
separate adjustment line on the projection.
