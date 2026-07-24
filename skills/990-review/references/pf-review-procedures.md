# 990-PF Review Procedures

Detailed mechanics for the checks in SKILL.md. Part references are to the 2021-and-later Form 990-PF revision.

## Part I column allocation

| Column | What belongs there | Watch for |
|---|---|---|
| (a) Revenue and expenses per books | Everything, tying to the financial statements | — |
| (b) Net investment income | Expenses directly attributable to producing investment income; **straight-line depreciation only** | Netted investment-advisor fees omitted; accelerated depreciation; federal income/excise taxes (never allowed) |
| (c) Adjusted net income | Completed for private operating foundations (and certain others); blank for most non-operating foundations | A POF with column (c) blank |
| (d) Disbursements for charitable purposes | Charitable expenses on the **cash basis**, regardless of the foundation's overall accounting method | Accrued-but-unpaid grants; any depreciation (never allowed in (d)); federal taxes |

Dual-use expenses (staff time, rent, professional fees serving both investment and charitable functions) must be allocated on a reasonable, consistent, documented basis. Ask for the allocation workpaper — "same split as last year" without support is a MEDIUM finding.

Column (b) feeds the 1.39% excise tax; column (d) feeds qualifying distributions. Verify the columns before recalculating either — a misallocation makes both recalculations tie to wrong inputs.

## Part IV capital gains (net investment income)

- **Donated property later sold**: basis is the donor's carryover basis — not FMV at the date of gift, not book value. Tie to gift-acceptance or donor records.
- The donated-vs-purchased designation in column (b) must be completed for each disposition.
- **Line 7(b) can never be negative**: capital losses offset capital gains only — no netting against interest or dividends, no carryback, no carryforward.

## Part IX valuation inputs (minimum investment return)

The 5% recalculation is only as good as its FMV inputs:

- Marketable securities: monthly-average FMV, with a consistent valuation date and method year over year.
- Cash: average of monthly balances (less the allowed cash-held-for-charitable-activities exclusion).
- Real estate and other non-marketable assets: consistent method; independent appraisal for real estate no more than five years old.
- Exempt-function (charitable-use) assets excluded; dual-use assets allocated with documentation.
- Short tax year: prorate the distributable amount.

## Qualifying-distribution qualification (Part XI)

Counted distributions must actually qualify:

- Grants to organizations **controlled** by the foundation or its disqualified persons do not count until the grantee redistributes them.
- Grants to **non-functionally-integrated Type III supporting organizations** do not count — and are taxable expenditures unless expenditure responsibility was exercised.
- **Recoveries** of amounts treated as qualifying distributions in a prior year are added back (Part X).
- **In-kind property distributions** count at FMV; the FMV-over-basis excess shows up as a Part III reconciling item.
- **PRIs** count if they meet IRC 4944(c) — see the red flag in SKILL.md.

## Disqualified-person list (IRC 4946)

Build the list before running the self-dealing screen:

- **Substantial contributors** — anyone whose cumulative gifts exceed $5,000 *and* 2% of the foundation's total contributions ever received. Check Schedule B against donor records for anyone who crossed the line **this year**; once a substantial contributor, effectively always one.
- Foundation managers (officers, directors, trustees, and anyone with similar powers).
- Owners of more than 20% of an entity that is itself a substantial contributor.
- Family members of any of the above (spouse, ancestors, children, grandchildren, great-grandchildren, and their spouses).
- Corporations, partnerships, and trusts in which the above hold more than 35%.

## Chapter 42 screens and Form 4720

| Section | Trigger | Screen |
|---|---|---|
| 4941 self-dealing | Any transaction with a disqualified person | Prohibited regardless of fairness or benefit to the foundation; check Part VI-B answers against the transaction detail |
| 4942 undistributed income | Qualifying distributions below the distributable amount | The Control Point in SKILL.md |
| 4943 excess business holdings | Foundation holds >2% of any business entity | Aggregate with disqualified persons' holdings against the 20% limit; 5-year clock to dispose of holdings received by gift or bequest; note the 4943(g) (philanthropic-business) and passive-investment exceptions before flagging |
| 4944 jeopardizing investments | Speculative or concentrated positions | Existing red flag; PRIs exempt when they meet 4944(c) |
| 4945 taxable expenditures | Lobbying; political spending; individual travel/study grants without an IRS-approved grant plan; grants to non-501(c)(3)s without expenditure responsibility; foreign grants without an equivalency determination or exercised expenditure responsibility (required attachment on the return) | Screen all expenditures, not just the grants list |
| 4960 excess compensation | Any employee's compensation over $1 million | 21% excise via Form 4720, regardless of reasonableness — a reasonable $1M+ salary still owes it |

Any hit: the finding must carry its consequence — **Form 4720** filing, correction within the correction period, and abatement consideration under IRC 4962 / reasonable cause. A Chapter 42 finding reported without the 4720 flag is incomplete.

## Initial-return branch (first-year foundations)

When the initial-return box is checked, or this is the foundation's first year:

- Determination letter received — or Form 1023 pending, with the filing date noted and the return posture consistent with pending status.
- **No prior-year carryovers** should appear (undistributed income, excess-distribution carryover, loss items). Any carryover on a first return is a finding.
- Distributable amount **prorated** for a short first year.
- Accounting method (Box J) affirmatively selected and consistent with the books; charitable disbursements still reported on the cash basis in column (d).
- Part VII lists every initial officer, director, and trustee — including unpaid ones at $0.
- Estimated-tax posture differs in year one (no prior-year-tax safe harbor exists) — confirm how payments were computed rather than assuming a safe harbor.
