---
name: 709-review
version: 1.0.0
description: |
  Cross-reference a completed Form 709 (U.S. Gift and Generation-Skipping Transfer Tax
  Return) against source documents — trust agreements, appraisals, Crummey notices,
  bank/wire records, prior-year 709s, and estate counsel's planning memos — to catch
  errors before filing. Verifies Schedule A part classification (direct skip vs.
  indirect skip vs. non-skip), GST automatic-allocation reconciliation on Schedule D,
  gift-splitting consent mechanics, §529(c)(2)(B) superfunding elections, Crummey
  present-interest support for ILIT contributions, and adequate disclosure for
  hard-to-value gifts. Use whenever a gift tax return needs a second set of eyes
  before it goes out the door — "review the 709", "check the gift tax return", "does
  the GST allocation look right", "tie out the gift tax return" — even if they don't
  say "GST" or "709".
trigger: |
  "review the 709", "gift tax return review", "check the gift tax return",
  "709 cross-reference", "tie out the gift tax return", "verify the 709",
  "does the GST allocation look right", "check the GST exemption",
  "second set of eyes on the 709", "review the gift return before we file",
  "Crummey letters", "ILIT gift review", "529 superfunding election",
  "gift splitting review"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 709 Review: Gift & GST Tax Return Cross-Reference

## Purpose

Catch errors before a Form 709 is filed. Gift tax returns fail differently than income tax returns: the numbers are usually small and simple, but the **classification, election, and allocation mechanics** are unforgiving and often irrevocable. A misclassified indirect skip, a missed election-out, or an unsigned gift-splitting consent doesn't change this year's tax — it silently spends GST exemption, breaks the statute of limitations protection, or invalidates the annual exclusion, and the error surfaces years later when it can no longer be fixed.

The deliverable is a severity-graded findings report tying every Schedule A and Schedule D entry to source documents. This is a technical review for a professional preparer; it does not replace the signing partner's sign-off.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

There is no percentage-based materiality threshold. On a 709, the dollar amounts are frequently *below* any income-tax materiality intuition — a $19,000 annual exclusion misapplied is a real error with real GST consequences regardless of how small it looks.

Classify findings by severity (impact + risk), not by dollar-amount materiality:

- **HIGH** — Wrong Schedule A part classification, missing or defective elections (election-out, §529(c)(2)(B), gift-splitting consent), GST allocation that doesn't reconcile, missing adequate-disclosure attachments for hard-to-value gifts, Crummey defects that defeat the annual exclusion
- **MEDIUM** — Documentation gaps (notices without proof of delivery, unverified extension filing), defensible-but-thin positions, items that could draw IRS correspondence
- **LOW** — Minor rounding, formatting/extraction artifacts (EIN/SSN formatting inconsistencies), presentation preferences

Report every discrepancy outside the rounding tolerance in the findings table, including items you are uncertain about. Severity ranks the list; it does not filter it. Coverage is the job at this stage — the preparer decides what to act on.

## Required Inputs

- Completed Form 709 draft and all schedules (A Parts 1–4, B, C, D Parts 1–3) with attachments
- Trust agreements for every trust receiving a gift (the actual instrument, not a summary)
- Gift substantiation: bank/wire records, checks, premium invoices, trust receipts
- Prior-year Form 709s (for prior taxable gifts, exemption already used, election continuity)
- Qualified appraisals for any hard-to-value gift (LLC/closely-held interests, real estate)
- Crummey notices and proof of delivery, if the return relies on withdrawal rights for the annual exclusion
- Spouse's Form 709 draft, if gift-splitting is elected
- Estate counsel's planning memo, if one exists (see Stage 1)

If a required input is missing, say so before starting rather than reviewing around the gap. A 709 review run without the trust agreement cannot verify skip classification or GST trust status — those findings would be guesses.

## Workflow

The engagement has two stages. Stage 1 applies only when the return hasn't been prepared yet (or a planning memo needs translating); Stage 2 is the core review and mirrors the other review skills.

### Stage 1 — Memo-to-return-prep translation *(when applicable)*

When outside counsel's planning memo is provided ahead of or alongside return prep, extract the concrete return-preparation mechanics from the narrative analysis:

1. **Donor/donee breakdown** — Who gave what to whom, in what amounts, on what dates, from what funding source (confirm the funding source — memos assume; bank records prove).
2. **Schedule A placement per gift** — Direct skip (Part 2), indirect skip to a GST trust (Part 3), or non-skip (Part 1). See `references/gst-mechanics.md` for the classification rules.
3. **Elections required** — §529(c)(2)(B) superfunding, gift-splitting under §2513, GST election-out or affirmative allocation.
4. **The automatic-allocation trap** — Planning memos frequently frame GST protection as "something to decide later." For indirect skips to GST trusts, that framing is wrong: §2632(c) allocates exemption automatically and irrevocably unless the donor elects out on a timely return. Surface this explicitly whenever the memo defers the GST decision.
5. **Missing items list** — Valuations, funding confirmations, gift-splitting intent, beneficiary information.

Output of Stage 1 is a return-prep action list, not a review report.

### Stage 2 — Return review

Read `references/gst-mechanics.md` before starting — the classification and allocation rules are where 709s quietly go wrong. If the return involves an ILIT or any trust relying on Crummey withdrawal rights for the annual exclusion, also read `references/ilit-crummey-review.md`.

1. **Verify donor information and filing posture** — Donor identity, tax year, individual vs. gift-splitting filing. If gift-splitting is elected: Part III consent completed, **signed Notice of Consent attached** (the software pre-checks the box; the signature is a separate requirement), and both spouses' returns show matching, complementary halved entries.
2. **Tie every gift to source documents** — Each Schedule A entry ties to bank/wire records, checks, premium payments, or trust receipts. Gift descriptions are accurate and complete (trust name, date, EIN, trustee, beneficiaries).
3. **Verify Schedule A part classification** — For every trust/entity gift, confirm direct skip (Part 2) vs. indirect skip (Part 3) vs. non-skip (Part 1) against the actual trust instrument. This is the most common consequential error on a 709. Whether a trust is a "GST trust" under §2632(c)(3)(B) turns on six technical statutory exceptions — read the instrument, don't pattern-match on "trust for a child."
4. **Verify annual exclusions (Schedule D Part 1 and Schedule A Part 4)** — Exclusions match what's actually available per donee (watch split-gift halving). For gifts in trust claiming the exclusion via Crummey powers, work the present-interest analysis in `references/ilit-crummey-review.md` — notice, withdrawal period, lapse mechanics, 5-and-5 / hanging powers.
5. **Verify §529(c)(2)(B) superfunding elections** — Box checked on Schedule A Part 4 Line B; statement attached with per-beneficiary, per-year breakdown; total doesn't exceed 5× the exclusion actually available (check for other gifts to the same beneficiary that already used room); ratable 1/5 reported in the correct Part (Part 1 for non-skip beneficiary, Part 2 for skip beneficiary). Confirm whether spouses each contributed their own 5× or gift-split one contribution — it changes whose return reports what.
6. **Reconcile GST allocation (Schedule D Part 2)** — If Schedule A Part 3 has entries and no election-out statement is attached, Line 5 must show the automatic allocation and Line 8 (exemption remaining) must be reduced accordingly. Verify this reconciles across both spouses' returns for split gifts — each spouse's own exemption is separately consumed. If an election-out statement is attached, confirm it covers the intended transfers and the return is timely (the election is only effective on a timely filed return).
7. **Verify the tax computation (Schedule D Part 3 and Part 2 of page 1)** — Inclusion ratio computed correctly; taxable gifts × rate table = tax; applicable credit ties to the current year's basic exclusion amount; prior taxable gifts tie to prior-year 709s; $0 balance due only where expected.
8. **Verify adequate disclosure** — For every hard-to-value gift: qualified appraisal attached, trust agreement attached, description sufficient under Treas. Reg. §301.6501(c)-1(f). This is what starts the statute of limitations; a return without it leaves the valuation open forever.
9. **Verify timeliness** — If the transmittal cites an extended due date, confirm Form 4868/8892 was actually and timely filed. Don't trust the software's "extended" checkbox.
10. **Summarize findings** — Produce the severity-graded report (see Output Format).
11. **Audit risk assessment** — Note 1–3 items presenting elevated audit risk, stated as facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop and get a human decision — these are planning judgments or hard stops, not mechanical checks:

- **Election out of automatic GST allocation (or affirmative allocation)** — Whether to let automatic allocation stand or elect out is a client planning decision with irrevocable consequences. Flag the deadline (due date of the return, with extensions) and present the trade-off; never resolve it silently.
- **GST trust status under §2632(c)(3)(B)** — Whether a specific trust falls into one of the six statutory exceptions requires reading the actual trust instrument. If the instrument is ambiguous or missing, this is a hard stop.
- **Gift-splitting consent missing** — A pre-checked box without the spouse's signed consent is not an election. Do not treat the return as fileable until the signed Notice of Consent exists.
- **Missing appraisal on a hard-to-value gift** — Without adequate disclosure the statute never starts. Hard stop until the appraisal and instrument are attached or the preparer accepts the exposure explicitly.
- **Crummey defect that would defeat the annual exclusion** — If notices weren't given, weren't timely, or the withdrawal right is illusory, the exclusion may not be available; the preparer decides whether to claim it anyway with disclosure or restructure the reporting.

## Red Flags

Pause and surface to the reviewer when:

- A trust gift is on Schedule A Part 1 but the trust could benefit skip persons — possible misclassified indirect skip
- Schedule A Part 3 has entries but Schedule D Part 2 Line 5 is zero and no election-out statement is attached
- An election-out statement is attached but the return is (or may be) late — the election may be ineffective
- Gift-splitting box checked but no signed spousal consent, or the spouse's return is missing/inconsistent
- 529 contributions exceed 5× the annual exclusion, or other gifts to the same beneficiary eat into the superfunding room
- Annual exclusion claimed for a gift in trust with no Crummey power, no notices, or notices without proof of delivery
- Withdrawal rights lapse in excess of the 5-and-5 limit with no hanging-power provision — powerholder gift exposure under §2514
- Minor beneficiaries hold withdrawal rights with no guardian notice
- Prior-year 709 shows exemption used that doesn't tie to this year's Schedule B / Schedule D carryforward
- Hard-to-value gift with no appraisal, a stale appraisal, or an appraisal that doesn't match the reported value
- The planning memo's GST discussion contradicts what the return actually does (e.g., memo says "defer the GST decision" while the return silently auto-allocates)
- Reliance on the 529/GST annual exclusion position — supported by Prop. Treas. Reg. §1.529-5(b) and practitioner consensus, but the regulation was never finalized; flag it as well-supported-not-bulletproof rather than smoothing over it

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., Rev. Rul., or procedure if applicable]
```

For each issue, classify the nature of the finding: **clear technical error**, **potential issue requiring further fact-gathering**, **judgment call / disclosure recommendation**, or **no issue noted** (for items specifically checked and cleared where the preparer would expect commentary).

Organized into sections:
- **Confirmed** — Entries that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by consequence for preparer attention
- **Missing Support** — Source docs absent (trust instruments, notices, appraisals, proof of extension)
- **Preparer Questions** — Items requiring judgment or client facts
- **Missing Information Request List** — Concise client/trustee/attorney request list (transfers confirmation, checks/wires, premium invoices, Crummey notices + proof of delivery, confirmation no withdrawal right was exercised, beneficiary information, prior 709s, gift-splitting intent, GST allocation intent)
- **Audit Risk Items** — 1–3 items with factual risk assessment
- **Reviewer Conclusion** — Ready to file / ready subject to minor changes / not ready, plus the top 3–5 items that must be resolved before filing

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 709", donor name, gift tax year, preparer name, review date
2. **Executive summary / bottom line** — 2-3 sentences plus the ready-to-file conclusion
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount, Nature (error / fact-gathering / judgment). Use `Table Grid` style
4. **GST allocation reconciliation** — Show the Schedule D Part 2 math explicitly (exemption available, automatic allocation, remaining), per spouse if split
5. **Crummey / present-interest analysis** *(ILIT returns)* — Notice status per beneficiary, lapse analysis
6. **Missing support** — Bulleted list
7. **Missing information request list** — Client-ready bulleted list
8. **Preparer questions** — Bulleted list
9. **Audit risk** — 1-3 bullet points, factual
10. **Reviewer conclusion** — Filing readiness and top items to resolve

Save as `[DonorName]_[GiftYear]_709_Review.docx` (e.g., `Smith_2025_709_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Handoffs

- **Substantive research** on whether a position is defensible (is this really a GST trust; should the client elect out; is a discount supportable) → `tax-advisor`
- **Client-facing explanation** of the return or the GST decision → `tax-memo` or `client-email`
- Stage 1 memo translation feeds return prep; this skill's Stage 2 then reviews the drafted return

## Safety Constraints

- Do not resolve the elect-out vs. auto-allocation decision yourself — present it with the deadline and consequences; the client and signing partner own it.
- Do not conclude GST trust status without reading the actual trust instrument; if it's missing, say so and stop.
- Do not opine on valuation or discount conclusions for closely-held interests — confirm a qualified appraisal is attached; whether the discount is right belongs to the appraiser and preparer.
- Do not assume facts not in the documents. If a conclusion depends on a missing fact (funding source, notice delivery, extension filing), state the dependency explicitly.
- Do not characterize audit risk as a probability or percentage. Judgment on acceptable risk belongs to the signing partner.
- Do not hardcode annual exclusion amounts, basic exclusion amounts, or GST exemption amounts — they change by year; reference the applicable year's figures.
- Verify authorities before citing them in findings; the authorities list in `references/gst-mechanics.md` was verified at the time of writing but must be re-verified for currency.
