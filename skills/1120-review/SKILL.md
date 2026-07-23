---
name: 1120-review
version: 1.7.0
description: |
  Cross-reference a completed Form 1120 (C-corporation income tax return) against its
  source documents — trial balance, supporting schedules, Form 4562, Form 3800, and the
  prior-year return — to catch errors before filing. Verifies income, deductions, credits,
  and the Schedule J tax computation tie out; reconciles Schedule M-1 book-to-tax and
  Schedule L / M-2; grades findings by severity; and flags audit-risk items including
  accumulated earnings tax (IRC 531) exposure. Use this whenever a C-corp return needs a
  second set of eyes before it goes out the door — "review the 1120", "tie out the C-corp
  return", "does the 1120 match the trial balance", "check the corporate return before we
  file" — even if they don't name the form or say the word "review".
trigger: |
  "review the 1120", "1120 review", "C-corp return review", "check the C-corp return",
  "1120 cross-reference", "tie out the C-corp return", "verify the 1120",
  "does the 1120 tie out", "check the 1120 before filing", "review the corporate return",
  "cross-reference the 1120 to the trial balance", "the C-corp return doesn't tie"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# 1120 Review: C-Corporation Return Cross-Reference

## Purpose

Catch errors in a Form 1120 before it is filed. Verify that income, deductions, credits, and the tax computation on the return tie to the trial balance and source documents, and surface anything that would draw IRS scrutiny. The deliverable is a severity-graded findings report a preparer can act on line by line.

This is a review, not a sign-off: findings go to the responsible preparer, who decides what to correct and owns the filed return.

## Accuracy Standard

Tax returns must be substantially correct. Rounding differences of $10 or less are acceptable (consistent with IRS whole-dollar rounding instructions and normal software rounding behavior). Beyond that, every discrepancy is a finding.

Do not apply a percentage-based materiality threshold — a percentage of gross receipts, total assets, or net income belongs in a financial-statement audit, not a tax review. A $2,000 error that changes the tax due is a real finding regardless of how small it is against total assets.

Classify each finding by severity (impact + risk), not by dollar-amount materiality:
- **HIGH**: Incorrect tax computation, wrong character of income, missing forms, positions without substantial authority
- **MEDIUM**: Documentation gaps, questionable positions that are defensible but need support, items that could trigger correspondence
- **LOW**: Minor rounding differences ($10-$100 range), presentation preferences, informational items

Report every discrepancy outside the rounding tolerance in the findings table — including items you are uncertain about or consider low-severity. Severity ranks the list; it does not filter it. Filtering happens at preparer review; your job here is complete coverage, because an error dropped now surfaces only after filing.

## Required Inputs

Confirm these are present before starting. A review run against a missing schedule or the wrong year's trial balance produces false comfort — the gaps look "clean" only because nothing was there to check.

- Completed Form 1120 and all schedules (C, D, E, J, K, L, M-1, M-2, M-3 if applicable)
- Trial balance or financial statements for the tax year
- Prior-year return (for NOL carryforwards, credit carryforwards, E&P)
- Any supporting workpapers

**PDF size check before ingestion:** if the return package or any source PDF exceeds ~500 pages, flag it and split it before reading — model PDF limits are 600 pages on ≥1M-context models and 100 pages otherwise (32 MB max). Silent truncation of a source document invalidates the review.

## Workflow

1. **Reconcile income and deductions to trial balance** — Tie Schedule M-1 book-to-tax differences. Flag unexplained items.
2. **Verify gross income** — Tie gross receipts and other income lines to the trial balance.
3. **Verify deductions** — Spot-check significant deductions (compensation, depreciation, interest) against supporting schedules or Form 4562.
4. **Verify credits** — Confirm each credit against the applicable form (Form 3800, etc.).
5. **Verify tax computation (Schedule J)** — Recalculate the tax liability. Confirm estimated tax payments and withholding. Check for accumulated earnings tax exposure (IRC 531) if retained earnings are growing without clear business purpose for the accumulation.
6. **Verify balance sheet (Schedule L)** — Tie beginning and ending balances. Flag unexplained changes.
7. **Verify retained earnings (M-2)** — Confirm beginning retained earnings ties to prior-year return. Verify current-year movements.
8. **Verify Section 199A / QBI reporting (if applicable)** — C-corporations are not pass-through entities and do not generate QBI for their shareholders. However, if the C-corp owns pass-through interests (partnership or S-corp K-1s), confirm:
   - QBI information from incoming K-1s is properly received and documented (the C-corp itself is not eligible for the 199A deduction, but the K-1 data should be retained for the entity's own records and for any ultimate owner-level QBI computation).
   - If the C-corp is a specified service trade or business (SSTB), note that its income does not qualify for 199A at the owner level — this affects any individual who might own the C-corp stock directly or through a pass-through.
   - No 199A deduction is claimed at the C-corp level — the QBI deduction is only available to individuals, trusts, and estates under IRC 199A.
9. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
10. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]."

## Control Points

Stop and route to the preparer before the return is treated as final when:

- **NOL carryforward** — An NOL deduction is taken. Confirm the carryforward amount ties to the prior-year return or NOL schedule; an unsupported carryforward is a common examination adjustment.
- **Any discrepancy beyond rounding** — Every variance beyond the $10 rounding tolerance needs preparer review and correction before filing. Do not resolve it yourself; the preparer owns the return.

## Red Flags

- Book income and taxable income reconciliation has unexplained permanent or timing differences
- Depreciation on the return significantly exceeds Form 4562
- Large dividend deduction (DRD) without supporting ownership documentation
- Prior-year credit carryforwards with no supporting schedule
- Accumulated earnings appear to exceed reasonable business needs — IRC 531 exposure
- Related-party transactions present without supporting transfer pricing documentation
- Cross-return coordination needed: if the corporation owns pass-through interests, K-1 income should tie to the issuing entity's return

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X]
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Confirmed** — Line items that tie
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW), ranked by dollar impact for preparer attention
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment
- **Audit Risk Items** — 1-3 items with factual risk assessment

### .docx Output

**Always produce a Word document (.docx) as the review deliverable.** The chat response gives the bottom-line summary; the .docx is the artifact the preparer works from and the firm keeps on file.

Use `python-docx` to build the document. Structure:

1. **Header** — Firm name, "Tax Return Review", "Form 1120", client/Corporation name, tax year, preparer name, review date
2. **Bottom line** — 2-3 sentence summary
3. **Findings table** — One row per issue: #, Severity (HIGH/MEDIUM/LOW), Line/Schedule, Description, Amount. Use `Table Grid` style
4. **Missing support** — Bulleted list of absent source documents
5. **Preparer questions** — Bulleted list of items requiring judgment
6. **Audit risk** — 1-3 bullet points, factual
7. **199A/QBI verification** — Summary of the QBI check results (no 199A at C-corp level; incoming K-1 QBI data documented; SSTB note)

Save as `[ClientName]_[TaxYear]_1120_Review.docx` (e.g., `ABCCorp_2025_1120_Review.docx`).

Key python-docx patterns:
- `doc.add_paragraph(text)` with `paragraph.style = 'Normal'` for body text
- `doc.add_table(rows, cols)` with `table.style = 'Table Grid'` for the findings table
- Bold the header row and severity column
- Use `doc.add_heading(text, level=1)` for section titles

Write the generation script to a file and run it via `Bash` with the system Python — do not try to generate the .docx inline in the chat.

## Safety Constraints

- Do not mark the return reviewed-complete while any discrepancy beyond rounding is unresolved — a "clean" review with open variances misleads the preparer into filing.
- State audit risk as facts, not as a probability or percentage ("this item may draw scrutiny because…"). Judging what level of risk is acceptable is the signing partner's call, not the reviewer's.
- Do not invent authority. Cite an IRC §, regulation, or procedure only when you are confident it applies; otherwise describe the issue and leave the citation for the preparer to confirm.
