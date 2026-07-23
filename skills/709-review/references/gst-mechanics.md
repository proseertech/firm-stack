# GST Mechanics for 709 Review

Domain knowledge for classifying gifts and reconciling GST exemption on Form 709.
Captured from a real engagement (trust-owned 529 superfunding + indirect-skip LLC
gifts to grantor trusts). Re-verify authority currency before relying on citations.

## 1. Direct skip vs. indirect skip vs. GST trust

- **Direct skip** — an outright transfer to a skip person (2+ generations below the
  donor) or a trust where *all* interests are held by skip persons. Reported on
  **Schedule A, Part 2**.
- **Indirect skip** — a transfer to a "GST trust" (§2632(c)(3)(B)) that is not a
  direct skip — typically a trust for a non-skip person (e.g., a child) that could
  later benefit a skip person (e.g., grandchildren). Reported on **Schedule A, Part 3**.
- **GST trust (§2632(c)(3)(B))** — broadly, any trust that could have a
  generation-skipping transfer with respect to the transferor, subject to **six
  statutory exceptions** (mostly involving mandatory distributions/withdrawal rights
  to non-skip persons before age 46, or estate inclusion). If a trust doesn't fall
  into one of the exceptions, it is a GST trust **by default**. The definition is
  broad and the exceptions are technical enough that many practitioners prefer an
  affirmative election either way rather than relying on the default.

**Review implication:** classification requires reading the actual trust instrument
against the six exceptions — never pattern-match on "trust for a child."

## 2. Automatic allocation of GST exemption — the single most-missed mechanic

- **§2632(b)** — automatic allocation to **direct skips**.
- **§2632(c)** — automatic allocation to **indirect skips** made to a GST trust. Key facts:
  - Applies **whether or not a Form 709 is filed** — the allocation happens by
    operation of law.
  - Effective as of the date of transfer; **irrevocable after the due date (with
    extensions)** of the Form 709 for the year of transfer.
  - To prevent it, the donor must **affirmatively elect out** on a timely Form 709
    (attach an "Election Out" statement) — silence means the exemption gets used.

A client/advisor conversation that frames GST protection as "something we'll do
later if we want it" is usually **wrong** for indirect skips to GST trusts — the
exemption is already being spent unless someone opts out in time. Planning memos
get this wrong routinely; surface it whenever a memo defers the GST decision.

**Review checkpoint:** if Schedule A, Part 3 has entries and there's no election-out
statement attached, **Schedule D, Part 2, Line 5** should show the automatic
allocation amount, and **Line 8** (exemption available for future transfers) should
be reduced accordingly. Verify this reconciles — including across split-gift
returns, where **each spouse's own exemption is separately consumed**.

## 3. GST annual exclusion and 529 plans

- **§2642(c)**: a direct skip that is a *nontaxable gift* (qualifies for the gift
  tax annual exclusion) gets an inclusion ratio of zero — informally the "GST
  annual exclusion." For gifts **in trust**, §2642(c)(2) requires the trust have a
  sole beneficiary during that person's life and be included in their estate if
  they die first — **most trusts don't qualify**.
- **529 plan contributions are the exception that matters**: even though a 529
  account may be nominally owned by a trust, the contribution is treated as a gift
  of a present interest **directly to the designated beneficiary** under
  §529(c)(2)(A)(i) — *not* a gift in trust. Because it's not "in trust" for this
  purpose, the §2642(c)(2) trust restrictions don't apply, and a direct-skip 529
  contribution qualifies for the GST annual exclusion.
- **Caveat to flag, not smooth over**: this position rests on
  **Prop. Treas. Reg. §1.529-5(b)** (proposed, never finalized) plus general
  practitioner consensus — not a final regulation. Treat it as well-supported but
  not bulletproof when reviewing or advising.

## 4. §529(c)(2)(B) superfunding mechanics

- Lets a donor elect to spread a 529 contribution **ratably over 5 years**, so up
  to 5× the annual exclusion can be contributed in one year without using lifetime
  exemption or triggering gift tax.
- **Per-donee ceiling**: 5 × annual exclusion, **per donor**. For a $19,000
  exclusion (2025/2026): $95,000 single / $190,000 if both spouses each contribute
  their own $95,000. Note that the $190,000 can be reached either by each spouse
  making their own direct contribution or by gift-splitting one contribution —
  **confirm which actually happened**, since it changes whose 709 reports what.
- **Election mechanics on Form 709**:
  - Check the box on **Schedule A, Part 4, Line B** ("if you elect under section
    529(c)(2)(B)…").
  - Report **1/5 of the elected amount each year** — Part 1 of Schedule A if the
    beneficiary is a non-skip person, **Part 2 if the beneficiary is a skip person**
    (e.g., grandchild).
  - **Attach a statement**: beneficiary name, total amount contributed, and the
    amount for which the election is being made, broken out by year.
  - No additional gifts to that beneficiary during the 5-year window without
    exceeding the exclusion.
  - If no other gifts requiring a 709 are made in years 2–5 of the election, **no
    return is required for those years** just to report the ratable portion.

## 5. Form 709 structural map

| Section | Purpose |
|---|---|
| Schedule A, Part 1 | Gifts subject only to gift tax (non-skip donees) |
| Schedule A, Part 2 | Direct skips |
| Schedule A, Part 3 | Indirect skips / other transfers in trust |
| Schedule A, Part 4 | Taxable gift reconciliation; §529(c)(2)(B) election box (Line B) |
| Part III (page 2) | Spouse's consent to gift-splitting (§2513); requires a **signed Notice of Consent attached**, not just the box checked |
| Schedule D, Part 1 | GST transfers with nontaxable portions (from annual exclusion) |
| Schedule D, Part 2 | GST exemption reconciliation — maximum exemption, amount used, automatic allocation to Part 3 transfers (Line 5), exemption remaining (Line 8) |
| Schedule D, Part 3 | Tax computation — inclusion ratio × 40% rate × net transfer |

**Adequate disclosure** for hard-to-value assets (LLC/closely-held interests):
attach a qualified appraisal and the underlying trust agreements. This is what
starts the statute of limitations running on gift tax valuation
(Treas. Reg. §301.6501(c)-1(f)).

## 6. Verified authorities

Confirmed via search during the source engagement — **re-verify currency before
relying on them again**:

- IRC §2503 / Treas. Reg. §25.2503-3 — annual exclusion, present interest, future interest definition
- IRC §2642(c) — GST annual exclusion (zero inclusion ratio for nontaxable direct skips); §2642(c)(2) trust exception
- IRC §529(c)(2)(A), (B) — present-interest treatment of 529 contributions; 5-year ratable election
- Prop. Treas. Reg. §1.529-5(b) — GST treatment of 529 accounts (**proposed, not finalized**)
- IRC §2632(b) — automatic allocation to direct skips
- IRC §2632(c)(1)–(3) and 26 CFR §26.2632-1 — automatic allocation to indirect skips, GST trust definition, election-out mechanics and irrevocability
- Instructions for Form 709 (applicable gift year) — Schedule A part placement rules (Part 1 vs. Part 2 for the ratable 529 portion; Part 3 for indirect skips), Schedule D Part 2 automatic-allocation reporting
