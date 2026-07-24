# Loss-Limitation Tiers and Transactional Events

Detailed procedures for workflow steps 5, 7, and 8. These are the checks the trial-balance reconciliation cannot see: a return can tie perfectly and still allocate a non-deductible loss, misreport a distribution, or skip a required transfer filing.

## 1. Loss-limitation tiers beyond basis

Section 704(d) basis is the first of three entity-visible gates. Work them in order — clearing one does not clear the next.

### At-risk (IRC 465)

- The at-risk amount is generally outside basis **minus** nonrecourse liabilities — except **qualified nonrecourse financing** on real property, which counts. This is why the K-1 Item K three-way split matters: a liability misclassified between nonrecourse and QNR silently changes every partner's at-risk amount.
- Check the at-risk **aggregation checkbox** (Form 1065, page 1, Item K(1)): if activities are aggregated for at-risk purposes, the box must be checked and the aggregation must be permissible.
- A partner guarantee (Item K3 checkbox) generally makes the guaranteed portion recourse to that partner — which raises their at-risk amount and lowers everyone else's.

### Passive activity (IRC 469)

- Check the passive-activity **grouping checkbox** (Item K(2)) and confirm grouping is **consistent with prior year** — regrouping requires a material change in facts and a disclosure statement.
- K-1s must report **activity by activity** where the partnership conducts more than one activity (or rentals plus a trade or business): separate statements of income/loss per activity, so each partner can apply §469 at their level. A single netted number on a multi-activity K-1 makes every partner's passive computation wrong.
- **Self-rental**: rental income from property leased to a business in which the partner materially participates is recharacterized as non-passive (income only — losses stay passive). Flag rentals to related operating entities.
- Rental activities are per-se passive regardless of participation (subject to the real-estate-professional rules applied at the partner level — not the partnership's call to make).

## 2. Distributions

Test **every** distribution, not just the total rolled through capital accounts:

1. **Cash over basis** — Cash (and deemed cash from liability shifts under §752) exceeding the distributee's outside basis triggers **§731(a) gain**. The capital-account roll will not show this; compare each distribution to that partner's outside basis at the time of distribution.
2. **Marketable securities** — Treated as cash under **§731(c)** (with exceptions for investment partnerships and the distributee's share of appreciation). A securities distribution reported as a tax-free property distribution needs the exception identified.
3. **Property distributions — Form 7217** — New for 2025: each partner receiving a property distribution files **Form 7217** reporting the basis of distributed property. Confirm the partnership furnished the information partners need (partnership basis in the property, any §732(a)(2)/(b) basis limitation where outside basis is less than the property's inside basis).
4. **§737 mixing-bowl gain** — If the distributee contributed appreciated property within the prior **seven years** and now receives *other* property, precontribution gain is recognized up to the excess of distributed value over outside basis.
5. **§704(c)(1)(B)** — The mirror image: property a partner contributed that is distributed to a **different** partner within seven years triggers gain/loss to the contributor.
6. Confirm distributions are reflected consistently in: K-1 Item L (withdrawals), Schedule M-2, and the basis/at-risk computations above.

## 3. Transfers of partnership interests

When any interest changed hands during the year (sale, exchange, gift, death):

- **K-1 Item J** — Beginning/ending percentages must reflect the transfer, and allocations must follow the varying-interest rules (interim closing or proration, consistently applied).
- **Form 8308** — Required for any sale or exchange when the partnership has §751(a) hot assets (unrealized receivables or inventory). The current form requires the transferor's share of **ordinary §751(a) gain, unrecaptured §1250 gain, and collectibles gain** — not just the fact of transfer. A missed or incomplete 8308 carries its own penalties.
- **Hot-asset analysis** — Flag for the preparer whether a §751(a) computation was actually performed; the selling partner's gain character depends on it, and "all capital gain" on a partnership with receivables or appreciated inventory is a red flag, not a default.
- **§754/§743(b)** — If a §754 election is in effect (or a substantial built-in loss forces it), confirm the §743(b) adjustment computation is attached and the adjustment is reported on the transferee's K-1 (Box 13 code V / Box 20 detail) — and **excluded** from tax-basis capital.

## 4. Section 704(c) detail

For property contributed with FMV different from tax basis:

- Identify the **allocation method** (traditional, traditional with curative allocations, or remedial) — the method is chosen property-by-property and must be applied consistently once chosen.
- Verify **depreciation allocations** follow the method: tax depreciation on contributed property goes first to non-contributing partners up to their book depreciation, with the ceiling rule (traditional) or curative/remedial fixes governing the shortfall.
- **K-1 Item N** — Net unrecognized §704(c) gain or loss, beginning and ending, is a mandatory disclosure the IRS matches. Blank Item N on a partnership with contributed appreciated property is a finding.
- Built-in-loss property: §704(c)(1)(C) limits the loss to the contributing partner; confirm the basis step-down mechanics if that partner's interest was transferred.
