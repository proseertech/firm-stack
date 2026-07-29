# Initial-Return Checklist (Year 1)

Run when the Initial Return box is checked on page 1, or the facts show this is the partnership's first filing year. Many first-year positions are made by *how the first return is filed* rather than by a separate statement — and several are irrevocable. The review's job is to confirm each decision was made deliberately, that the return actually reflects it, and that a statement is present **only where one is required**.

Terminology and box-code conventions follow the Terminology section of `SKILL.md`.

## Entity and classification

- **Entity classification** — Confirm the entity's default classification (domestic multi-member LLC → partnership) is what was intended; if a different classification was elected, Form 8832 was filed and the acceptance is in the file. If an intended election was missed, flag late-election relief (Rev. Proc. 2009-41) for the preparer — do not paper over it.
- **Header data** — Legal name, EIN (matches the IRS CP 575 notice), address, business code.
- **Formation date vs. business start date** — These are different dates and both matter:
  - The **formation date** is when the entity came into existence under state law.
  - The **business start date** (page 1, Item E) is when the partnership began business. It controls the return period's beginning and the month §709 amortization starts.
  - The date the **active trade or business begins** controls the month §195 amortization starts, and can be later than either of the above.
  - Costs incurred before the active trade or business begins are start-up costs; costs after are ordinary operating expenses. Confirm the return draws the line on the correct date.
- **Initial Return box** — Actually checked.

## Tax year and accounting method

- **Tax year** — Calendar year, the required year under §706(b) (majority-interest / principal-partners / least-aggregate-deferral), or a §444 election. If §444: Form 8716 filed, and the annual Form 8752 required-payment obligation noted for future years. A short first year affects depreciation and the amortization schedules below.
- **Accounting method** — The method adopted on this return *is* the election. Confirm cash vs. accrual is permissible under §448 (aggregate gross receipts at or below the §448(c) threshold on an aggregated basis, no C-corporation partner, and not a tax shelter) and that it matches how the books are kept or the M-1 explains the difference.
- **Syndicate test — run it once, apply it twice** — A partnership allocating more than 35% of losses to limited partners or limited entrepreneurs is a **syndicate**, therefore a tax shelter. That single conclusion (a) forces accrual accounting regardless of gross receipts and (b) disqualifies the partnership from the §163(j) small-business exception. A year-1 return using the cash method while also skipping Form 8990 is internally inconsistent — resolve which conclusion is right before sign-off.
- **Inventory method** — If inventories exist: method adopted (including the §471(c) small-taxpayer book-conformity method); LIFO requires Form 970 filed with this return.

## Start-up, organizational, and syndication costs

Do **not** look for a §195 or §709 election statement — the regulations deem the election made by return treatment. Test classification, mechanics, and deliberateness instead.

- **Three-way classification** — Every pre-operating and formation cost lands in exactly one bucket. A single "start-up and organizational costs" line with no split is a finding.
  - **§195 start-up** — Investigatory and pre-opening operating costs of the trade or business.
  - **§709 organizational** — Must meet §709(b)(3) / Reg. §1.709-2(a): incident to the creation of the partnership, chargeable to capital account, and of a character that would be amortized over the partnership's life if it had one (e.g., legal fees for the partnership agreement, state filing fees, accounting fees to set up the books).
  - **Syndication** — Costs of selling or issuing partnership interests: offering memoranda, promotional and marketing materials, brokerage and placement fees, registration fees, and the legal and accounting fees attributable to the offering. **Capitalized permanently** under Reg. §1.709-2(b) — not deductible, not amortizable, no 180-month schedule. Amortized syndication costs are a HIGH finding.
- **§195 mechanics** — Up to $5,000 deducted, reduced dollar-for-dollar to the extent start-up expenditures exceed $50,000; remainder amortized over 180 months beginning with the month the **active trade or business begins**. Deemed elected under Reg. §1.195-1(b) for that year.
- **§709 mechanics** — Up to $5,000 deducted, same $50,000 phase-down; remainder amortized over 180 months beginning with the month the **partnership begins business**. Deemed elected under Reg. §1.709-1(b)(2) for that year.
- **Confirm on the return** — The $5,000 (as limited) and the 180-month amortization actually appear, and each schedule starts in its own correct month. A 180-month schedule keyed to the formation date, or defaulted to January of the first year, is a finding.
- **Capitalization is a decision** — Forgoing the deemed election and capitalizing is **irrevocable** and applies to **all** costs in that category. If the return capitalizes, confirm it was deliberate and documented; if it appears to be a data-entry default, flag it while the return is still amendable in the year of election.
- **Watch the offering-heavy client** — A fund or syndicated real estate partnership will have large legal and accounting invoices spanning all three buckets. Ask for the invoice-level allocation, not the summary journal entry.

## Election statements — confirm attached where required

- **De minimis safe harbor** (Reg. §1.263(a)-1(f)) — Annual election statement attached if the fixed-asset policy relies on it.
- **Bonus depreciation elect-out** (§168(k)(7)) — If slower depreciation was intended for any class, the election-out statement must be attached; silence means bonus applies.
- **§179** — Elected on Form 4562, Part I; check the applicable year's limit, phase-out, and the taxable-income limitation, and note that each partner faces a separate limit on their own return.
- **§163(j)(7)(B) electing real property trade or business** — Common in year 1 for real estate partnerships and **irrevocable**. It requires ADS for nonresidential real property, residential rental property, and QIP — confirm the first-year fixed-asset register was actually set up on ADS, because a later correction means a method change.
- **§174A** — If domestic R&E is being capitalized and amortized rather than expensed, the election must be documented in year 1.
- **§754** — Rarely relevant in year 1, but if property came in with built-in disparities or an interest has already transferred, confirm the posture was considered; the election requires a signed statement with the return and binds later years.
- **§444** — Form 8716, if a fiscal year was elected.

## Capital, basis, and audit regime

- **Beginning tax-basis capital** — Must equal initial contributions (cash plus the tax basis of contributed property), with **no carryover balances**. A nonzero beginning balance on an initial return means either the box is wrong or the books imported another entity's history. Confirm the Item L method checkbox says tax basis, that the transactional roll (Notice 2019-66) is set up correctly from day one, and that §743(b) adjustments — if any ever arise — will sit outside tax-basis capital.
- **§704(c) tracking initiated** — Contributed property with FMV ≠ basis starts the §704(c) obligation now: allocation method chosen property-by-property, **Item M** answered, and **Item N** completed on the first return. Year 1 is when the layers are cheap to document and the only time the contribution facts are fresh. See `loss-limits-and-transactions.md` §4.
- **Partner basis inputs initiated** — The partnership should furnish the inputs partners need for outside basis from day one; reconstructing them years later is the single most common source of unsupportable loss deductions.
- **Liability allocations** — Initial §752 allocation consistent with the partnership agreement's economic arrangement, with the nonrecourse / QNRF / recourse split reported on Schedule K-1 Item K1, lower-tier liabilities identified in Item K2, and guarantees or deficit restoration obligations reflected in Item K3.
- **Entity-level checkboxes** — If the partnership will aggregate activities for §465 or group them for §469, the first-year position sets the baseline: page 1 Item K(1)/K(2) checked as applicable, and the groupings documented so later-year consistency can be tested.
- **BBA/CPAR posture** — Eligible small partnerships may elect out under §6221(b) on a timely filed return, which requires **Schedule B-2** listing every eligible partner (the all-eligible-partner test fails with a single partnership or trust partner). Otherwise a partnership representative must be designated. Confirm the choice was deliberate, not a software default.

## First-year §199A setup

The year-1 positions here get copied forward for the life of the entity, so verify them once, properly.

- **Trade-or-business identification** — Decide and document how many separate trades or businesses the partnership has; the Box 20 code Z statement must report QBI, W-2 wages, UBIA, and SSTB status for each. A blended year-1 statement becomes the template for every later year.
- **SSTB determination** — Documented, with the reasoning. Note that **engineering and architecture are excluded** from SSTB for §199A purposes — a professional-services partnership in those fields should not be flagged.
- **Rental activities** — If rental income is being treated as QBI, confirm the activity rises to a §162 trade or business or the Rev. Proc. 2019-38 safe harbor requirements (including the contemporaneous records requirement) are being met from the start.
- **Allocation bases established** — W-2 wages allocated in proportion to each partner's share of the **wage expense deduction**, and UBIA in proportion to **tax depreciation** — not by ownership percentage. In a partnership with special allocations or contributed property, these diverge in year 1 and stay diverged.

## First-year consistency checks

- Depreciation conventions (half-year vs. mid-quarter — a year-end asset spree triggers mid-quarter) and short-year depreciation if the first year is short.
- Bonus depreciation rate matched to each asset's **acquisition** date for 2025 additions (40% before January 20, 2025; 100% on or after), including assets acquired under a pre-January 20 written binding contract.
- Guaranteed payments, if any, are supported by the partnership agreement in effect during year 1, and split between services (line 4a) and capital (line 4b).
- Any partner compensation run through payroll — no partner should have a W-2.
- Filing mechanics for a first return: due date, Form 7004 if extended, e-file eligibility (a first-year return with a newly issued EIN is a common e-file rejection), Schedule B-1 if any owner holds 50% or more, and Schedules C/M-3 if the thresholds are met on day one from contributed assets.
- State registrations and first-year state filings match the operating footprint — route to Preparer Questions per the federal-only scope constraint.
