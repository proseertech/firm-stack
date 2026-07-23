---
name: 1120s-review
version: 1.7.0
description: |
  Cross-reference a completed Form 1120-S (S-corporation return) against its source
  documents — trial balance, Schedule K-1s, officer W-2s, Form 1125-E, and supporting
  schedules — to catch errors before filing. Verifies income, deductions, credits, and
  shareholder allocations, checks that K-1s foot to Schedule K, and flags audit-risk items
  including reasonable-compensation exposure. Use this whenever someone hands you a drafted
  or finished S-corp return and wants it checked, tied out, or reviewed against the books —
  "review the 1120-S", "does the S-corp return tie to the TB", "check the K-1 allocations",
  "second set of eyes on this S-corp before we file" — even if they don't name the form or
  say the word "review."
trigger: |
  "review the 1120-S", "review the 1120S", "S-corp return review", "check the S-corp",
  "1120-S cross-reference", "tie out the S-corp return", "verify the 1120S",
  "does the S-corp tie to the trial balance", "check the K-1 allocations",
  "reasonable comp check", "did we tie out the S-corp", "S-corp return before we file",
  "second look at the S-corp"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1120-S Review: S-Corporation Return Cross-Reference

## Purpose

Catch errors before a Form 1120-S is filed. Verify that income, deductions, and shareholder allocations on the return tie to the trial balance and source documents, and that each K-1 is mathematically consistent with the Schedule K totals. The deliverable is a severity-graded findings report a preparer can act on line by line.

## Accuracy Standard

A tax return must be substantially correct, so the bar here is different from a financial-statement audit — there is no percentage materiality. Do not use a percentage of gross receipts, total assets, or net income to decide whether a variance is acceptable; that test belongs to audit engagements, not tax review.

The only tolerance is rounding: differences of $10 or less are expected (consistent with IRS whole-dollar rounding and normal software behavior). Every discrepancy beyond that is a finding.

Grade findings by severity — impact plus risk, not dollar size:

- **HIGH** — Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM** — Documentation gaps, defensible-but-thin positions, items that could draw IRS correspondence
- **LOW** — Minor rounding ($10–$100 range), presentation preferences, informational items

Report *every* discrepancy outside the rounding tolerance, including low-severity or uncertain ones. Severity ranks the list; it does not filter it. Filtering understates coverage, and the item you drop as "probably fine" is the one that surfaces after filing. A separate preparer review decides what to act on — your job here is complete coverage.

## Required Inputs

- Completed Form 1120-S and all schedules (K, K-1s, L, M-1, M-2)
- Trial balance or financial statements for the tax year
- Officer W-2s and Form 1125-E
- Prior-year return (for AAA balance, basis, and carryforwards)
- Shareholder basis worksheets (if losses flow through)
- Any supporting workpapers

If a required input is missing, say so before starting rather than reviewing around the gap — a review that silently skips the basis worksheet or the prior-year return gives false assurance.

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

1. **Reconcile income and deductions to the trial balance** — Tie Schedule K ordinary income/loss to the book-to-tax reconciliation (M-1). Flag unexplained M-1 adjustments.
2. **Verify officer compensation** — Confirm officer wages on Form 1125-E tie to the W-2s. Compare officer compensation to distributions: if distributions materially exceed compensation, flag the reasonable-compensation issue. This is a well-known S-corp audit trigger — recharacterization as wages carries FICA employment-tax exposure under IRC 3111/3121, per the *David E. Watson, P.C.* line of cases.
3. **Verify Schedule K items** — Check each separately stated item (interest, dividends, Section 1231, credits, etc.) against source.
4. **Verify K-1 allocations** — Confirm each shareholder's K-1 totals sum to Schedule K. Verify ownership percentages against the shareholder agreement or prior-year return.
5. **Verify shareholder basis** — For each shareholder taking a loss, check that the K-1 loss does not exceed stock plus debt basis. Cross-reference the basis worksheet if provided; if a loss flows through and no worksheet exists, flag it as requiring basis documentation.
6. **Verify the balance sheet (Schedule L)** — Tie beginning and ending balances to the prior-year return and current trial balance. Flag unexplained changes.
7. **Verify AAA and M-2** — Confirm the AAA beginning balance ties to the prior-year return, and that current-year movements are correctly reflected.
8. **Verify Section 199A / QBI reporting** — The S-corp reports QBI information on each K-1 (Box 17, codes V through AC): QBI amount, W-2 wages (code W), and UBIA of qualified property (code AC). Confirm:
   - QBI amount on each K-1 equals the shareholder's share of ordinary income/loss from Schedule K (line 1), adjusted for separately stated income/gains that are excluded from QBI (e.g., Section 1231 gains, capital gains).
   - W-2 wage amount (code W) is correctly allocated among shareholders per ownership percentage (or an alternative method if documented).
   - UBIA of qualified property (code AC) is reported if the entity has qualified property.
   - SSTB classification: if the S-corp is a Specified Service Trade or Business, this must be disclosed on the K-1. The SSTB flag flows to the shareholder's 1040 for the 199A phase-out calculation. An incorrect SSTB classification can overstate or understate the shareholder's QBI deduction.
   - If the S-corp had a loss for the year, confirm the QBI amount on the K-1 reflects the loss (negative QBI reduces the shareholder's overall QBI).
9. **Summarize findings** — Produce the severity-graded report (see Output Format).
10. **Assess audit risk** — Note 1–3 items presenting elevated audit risk, stated as facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop for a preparer decision — don't quietly reconcile past these:

- **K-1 totals don't foot to Schedule K** — Allocations must equal the Schedule K totals. Any discrepancy is a hard stop; a return where the K-1s don't sum is not fileable.
- **Any discrepancy beyond rounding** — Every variance beyond the $10 rounding tolerance needs preparer review and correction before filing.
- **Shareholder loss without basis** — A loss flowing through without a basis worksheet is a hard stop; without basis substantiation the loss may be non-deductible.

## Red Flags

Pause and surface to the user when:

- Ordinary income/loss doesn't reconcile to the trial balance within a small rounding amount
- K-1 percentages don't match the shareholder agreement
- AAA goes below zero without a corresponding distribution-in-excess-of-basis being flagged
- Officer compensation appears unreasonably low relative to S-corp income
- Distributions to shareholders significantly exceed officer W-2 wages — reasonable-compensation risk
- Shareholder loss exceeds stock plus debt basis without a supporting basis schedule
- Prior-year credits or carryforwards appear with no schedule supporting the amount
- Cross-return coordination needed — K-1 amounts should tie to each shareholder's Form 1040, Schedule E

## Output Format

A structured findings report. Each issue reads:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into:

- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked within severity by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1–3 items with a factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120-S", client/S-Corp name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Missing support** — Bulleted list of absent source documents
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **199A/QBI verification** — Summary of the QBI check results (K-1 Box 17 codes V–AC, W-2 wage allocation, SSTB classification, loss QBI)

Save as `[ClientName]_[TaxYear]_1120S_Review.docx` (e.g., `ABCCorp_2025_1120S_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete while K-1 totals don't foot to Schedule K — the return isn't fileable and "complete" would be misleading.
- Do not adjust AAA or basis yourself — surface the issue for preparer review; those balances drive shareholder-level tax and are the preparer's call.
- Do not express audit risk as a probability or percentage. State the factual reason an item may draw scrutiny; judging acceptable risk is the signing partner's decision.
