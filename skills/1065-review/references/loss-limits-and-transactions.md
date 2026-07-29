# Loss-Limitation Tiers and Transactional Events

Detailed procedures for workflow steps 5, 7, and 8. These are the checks the trial-balance reconciliation cannot see: a return can tie perfectly and still allocate a non-deductible loss, misreport a distribution, skip a required transfer filing, or omit a mandatory §704(c) disclosure.

Terminology and box-code conventions follow the Terminology section of `SKILL.md`. **Verify any code cited here against the applicable year's Schedule K-1 instructions before reporting a code as wrong.**

**Scope of the entity-level review.** Every limitation below is ultimately computed on the *partner's* return. The partnership's obligation — and what this review tests — is whether the return furnishes accurate, correctly classified inputs: liability splits, guarantees, activity-by-activity results, grouping positions, distribution basis detail, and §704(c) amounts. Report missing or misclassified inputs as findings; do not present a partner-level conclusion as the partnership's.

## 1. Loss-limitation tiers

Three tiers, applied **in this order**. Clearing one does not clear the next, and each tier operates only on the loss that survived the tier above it.

### Tier 1 — Basis (§704(d), with outside basis under §705)

- A partner's distributive share of loss is allowed only to the extent of outside basis at the end of the partnership year. The excess is disallowed and carried forward until basis is restored.
- Outside basis = tax-basis capital + the partner's §752 share of liabilities, adjusted for current-year contributions, distributions, and allocated items.
- **Ordering matters downstream:** loss disallowed under §704(d) is **not** taken into account in applying §465 or §469. Only the portion that clears basis moves to the at-risk tier. A workpaper that runs at-risk or passive limits against the full allocated loss is wrong even if the arithmetic is clean.
- **EBIE reduces basis when allocated** — §163(j) excess business interest expense reduces the partner's outside basis in the year it is allocated, even though it is not currently deductible (§163(j)(4)(B)(iii)(I)). Confirm the basis inputs reflect it. On a later disposition of the interest, basis is increased immediately before the disposition by any EBIE never deducted (§163(j)(4)(B)(iii)(II)) — coordinate with §3 below.
- Entity-level check: the partnership supplied accurate basis inputs — beginning tax-basis capital tied to prior-year K-1s, contributions, tax-basis income/loss, distributions, allocated EBIE, and the liability split.

### Tier 2 — At-risk (§465)

- Deductions are limited to the amount the partner has at risk in the activity. Practical approximation: outside basis **minus** nonrecourse liabilities, **plus** qualified nonrecourse financing (QNRF) on real property under §465(b)(6). This is a **partner-level** computation — report inputs, not a conclusion.
- This is why the Schedule K-1 **Item K1** three-way split matters: a liability misclassified between nonrecourse and QNRF silently changes the at-risk amount on every affected K-1.
- **Item K2** — lower-tier partnership liabilities included in Item K1 must be identified.
- **Item K3** — guarantees and other payment obligations, including deficit restoration obligations (DROs), must be reported. A partner guarantee generally makes the guaranteed portion recourse to that partner, raising their at-risk amount and lowering everyone else's; an unreported DRO does the same thing invisibly.
- **Form 1065 page 1, Item K(1)** — the at-risk **aggregation** checkbox. If activities are aggregated for §465 purposes, the box must be checked and the aggregation must be permissible for those activities.
- Amounts protected against loss by guarantees, stop-loss agreements, or nonrecourse financing from a person with an interest in the activity are not at risk. Flag any such arrangement visible in the loan documents or agreement.

### Tier 3 — Passive activity (§469)

- Passive losses are deductible only against passive income; the excess is suspended and carried forward.
- **Form 1065 page 1, Item K(2)** — the passive **grouping** checkbox. Confirm it is checked where activities were grouped, and that the grouping is **consistent with prior year** — regrouping requires a material change in facts and circumstances and a disclosure statement.
- **Activity-by-activity K-1 reporting** — where the partnership conducts more than one activity (or rentals plus a trade or business), each K-1 must report income/loss separately by activity so the partner can apply §469. A single netted number on a multi-activity K-1 makes every partner's passive computation wrong. This is the same segregation §199A needs — reconcile with the Box 20 code Z statement.
- **Self-rental** — Rental income from property leased to an activity in which the partner materially participates is recharacterized as non-passive (income only; losses stay passive). The partnership's job is to **flag** the related-party rentals so partners can apply the rule; the recharacterization itself happens on the partner's return.
- **Rental activities** are per-se passive at the entity level. Real-estate-professional status and material participation are determined on the partner's return — not the partnership's call to make, and not something to conclude in this review.

## 2. Distributions

Test **every** distribution, not just the total rolled through capital accounts.

1. **Money over basis — §731(a)(1)** — Gain is recognized when money distributed to a partner exceeds the partner's adjusted basis in the partnership interest immediately before the distribution. "Money" includes **deemed** distributions from a decrease in the partner's share of liabilities under §752(b). The gain is generally capital (treated as from the sale or exchange of the interest), subject to recharacterization where §751 hot assets are involved. The capital-account roll will not show this — compare each distribution to that partner's outside basis at the time of distribution.
2. **Loss — §731(a)(2)** — Loss is **not** recognized on a nonliquidating distribution. Loss is recognized only on a distribution in **liquidation** of the partner's entire interest, and only where the distributed property consists **solely of money, unrealized receivables, and inventory**. A recognized loss on any other fact pattern is a finding.
3. **Marketable securities — §731(c)** — Generally treated as money, and therefore capable of triggering §731(a)(1) gain. Exceptions exist (investment partnerships, the distributee's share of the securities' appreciation, previously contributed securities). A securities distribution reported as a tax-free property distribution requires the specific exception to be identified in the file — "it's property" is not an answer.
4. **Property distributions — Form 7217** — Beginning with 2025, a partner receiving a distribution of property files **Form 7217** reporting the basis of the distributed property. Confirm the partnership furnished what the partner needs: the partnership's basis in each distributed asset, the distribution date, and any §732(a)(2) or §732(b) basis-limitation detail where the partner's outside basis is less than the partnership's inside basis in the property. A property distribution with no basis information furnished is a finding against the partnership even though the form is filed by the partner.
5. **Disproportionate distributions — §751(b)** — A distribution that shifts a partner's interest in hot assets relative to other property is recast as a taxable exchange, producing ordinary income. Screen any non-pro-rata distribution in a partnership holding receivables or appreciated inventory; a pro-rata assumption stated nowhere in the file is not support.
6. **§737 mixing-bowl gain** — If the distributee **contributed appreciated property within the prior seven years** and now receives *other* property, net precontribution gain is recognized, limited to the excess of the distributed property's value over the partner's outside basis.
7. **§704(c)(1)(B) — the mirror image** — Property a partner contributed that is distributed to a **different** partner within seven years triggers gain or loss to the **contributing** partner, as if the property had been sold at FMV.
8. **§734(b)** — Where a §754 election is in effect (or a substantial basis reduction applies), a distribution can trigger an inside-basis adjustment to the partnership's remaining assets. Confirm the computation exists and is allocated under §755; unlike §743(b), a §734(b) adjustment is a common-basis adjustment, not transferee-specific.
9. **Consistency** — Confirm distributions are reflected consistently across K-1 Item L (withdrawals and distributions), Schedule M-2, and the basis / at-risk inputs above. A distribution that appears in one and not the others is a finding regardless of which one is right.

## 3. Transfers of partnership interests

When any interest changed hands during the year (sale, exchange, gift, death), there are three separate tasks. Do all three — they fail independently.

### 3a. Ownership and allocations

- **K-1 Item J** — Beginning and ending profit, loss, and capital percentages must reflect the transfer for both the transferor and the transferee, and the "decrease due to sale or exchange of partnership interest" checkbox must be marked where applicable. That checkbox and a missing Form 8308 are a direct contradiction.
- **§706 varying-interest allocations** — Allocations must follow either the interim-closing-of-the-books method or the proration method, applied **consistently**, with the convention documented. Check that the transferor's and transferee's allocations sum to the full-year amount with no gap or overlap, and that extraordinary items were allocated to the date they occurred.
- **Basis restoration for unused EBIE** — A transferor's basis is increased immediately before disposition by EBIE that was never deducted (§163(j)(4)(B)(iii)(II)). Confirm the basis inputs furnished for the transferor reflect it; missing it overstates the transferor's gain.

### 3b. Hot assets and Form 8308

- **§751(a) computation** — Required where the partnership holds hot assets: unrealized receivables and **substantially appreciated** inventory. Confirm the computation was actually performed and is in the file; the selling partner's gain character depends on it.
- **Form 8308** — Required for any sale or exchange of an interest where §751(a) hot assets exist. The current form requires more than the fact of transfer: the transferor's share of **ordinary §751(a) gain or loss, unrecaptured §1250 gain, and collectibles gain**, furnished to the transferor and transferee as well as filed with the return. The same three character items are the Box 20 code AB / AD / AC detail on the transferor's K-1 — they must agree. A missed or incomplete 8308 carries its own penalties.
- **Red flag** — "All capital gain" reported by a transferor in a partnership with receivables or appreciated inventory is a red flag, not a default.

### 3c. §754 election and §743(b) adjustment

- Applies where a §754 election is in effect, or where a **substantial built-in loss** at the time of transfer mandates the adjustment regardless of election.
- **Computation in the file** — The §743(b) adjustment is transferee-specific: the difference between the transferee's outside basis and their share of the partnership's inside basis, allocated among assets under §755. Confirm the computation exists and is asset-by-asset, not a single plug.
- **K-1 reporting** — Report the transferee's §743(b) income effect using the designated codes: positive adjustments in Box 11 (code F) and negative adjustments in Box 13 (code V), with the corresponding amounts carried on Schedule K and the adjustment itself disclosed in the Box 20 "other information" detail. **Confirm the current code letters in the applicable year's Schedule K-1 instructions** — the §743(b) Box 20 assignment has moved across form years, and the software default may cite a code that has since been reassigned.
- **Excluded from tax-basis capital** — §743(b) adjustments are tracked on a separate schedule and never folded into the transferee's tax-basis capital. Embedded 743(b) misstates that partner's capital every year thereafter.

### 3d. Foreign transferors

- **§1446(f)** — A foreign partner's transfer of an interest in a partnership engaged in a US trade or business triggers 10% transferee withholding on the amount realized, with a **secondary withholding obligation on the partnership** if the transferee failed to withhold. Confirm withholding, a valid certification/exception, or the partnership's own filing.
- **§864(c)(8)** — The foreign transferor's gain is ECI to the extent attributable to the partnership's US trade or business. Confirm the partnership furnished the information the transferor needs, and coordinate with the §1446(a) and K-2/K-3 checks in workflow step 12.

## 4. Section 704(c) detail

For property contributed with FMV different from tax basis:

- **Allocation method** — Identify it **property-by-property**: traditional, traditional with curative allocations, or remedial. Once chosen for an item of property, the method must be applied consistently; a partnership may use different methods for different properties, but not different methods for the same property year over year.
- **Depreciation allocations** — Verify they follow the chosen method: tax depreciation on contributed property goes first to the **non-contributing** partners up to their book depreciation, with the ceiling rule (traditional), curative allocations of other items, or remedial notional items governing the shortfall.
- **Gain allocations** — On disposition, built-in gain or loss goes to the contributing partner first, to the extent it remains.
- **K-1 Item M and Item N** — Item M ("Did the partner contribute property with a built-in gain or loss?") and Item N (net unrecognized §704(c) gain or loss, **beginning and ending**) must agree; "Yes" in M with a blank N contradicts itself on the face of the K-1. Item N is a **mandatory disclosure** for any partnership holding §704(c) property and the IRS matches it — a blank is a finding. Item N must also **reconcile to the internal §704(c) tracking schedule**; a populated Item N that doesn't tie to the underlying layers is a finding too, and the more common one.
- **QBI interaction** — UBIA of qualified property is allocated in proportion to **tax depreciation** (Reg. §1.199A-2(a)(3)), so a curative or remedial method — or the ceiling rule under the traditional method — changes each partner's UBIA away from ownership percentage. Reconcile the Box 20 code Z statement against the §704(c) depreciation allocations; UBIA spread pro-rata in a §704(c) partnership is a finding on both steps.
- **Built-in-loss property** — §704(c)(1)(C) limits the built-in loss to the contributing partner; the property has a different basis for the other partners. Confirm the basis step-down mechanics if that partner's interest was transferred.
- **Reverse §704(c)** — Revaluations on the entry or exit of a partner create reverse §704(c) layers subject to the same method-consistency and Item N tracking. Confirm layers created in prior years are still being tracked, not dropped at a software conversion or a change of preparer.
