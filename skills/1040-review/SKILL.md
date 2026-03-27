---
name: 1040-review
version: 1.1.0
description: |
  Cross-reference a completed Form 1040 (individual income tax return) against
  source documents — W-2s, 1099s, K-1s, brokerage statements, and supporting
  schedules — to verify every income, deduction, credit, and withholding line
  ties back correctly. Quantifies materiality, grades findings by severity,
  and flags audit risk items.
trigger: |
  "review the 1040", "check the individual return", "1040 cross-reference",
  "tie out the 1040", "verify the individual return"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# 1040 Review: Individual Return Cross-Reference

## Purpose

Catch errors before a Form 1040 is filed. Verify that every material line on the return ties to a source document and that no income, deduction, or credit has been omitted or misstated.

## Required Inputs

- Completed Form 1040 (PDF or data export)
- All source documents: W-2s, 1099s (INT, DIV, B, R, SSA, MISC, NEC), K-1s, brokerage statements
- Any supporting workpapers or schedules
- Basis worksheets for pass-through entities (if losses are claimed)

## Workflow

1. **Establish materiality and scope** — Quantify materiality for this return. Use the firm's configured materiality threshold; if not configured, use 2% of total gross income as working materiality. Every finding in subsequent steps is classified as material or immaterial relative to this threshold.
2. **Inventory source documents** — List all source docs provided. Flag any that appear to be missing based on the return (e.g., K-1 income on Schedule E with no K-1 provided).
3. **Verify wages and compensation** — Tie W-2 Box 1 wages to Line 1a. Check Box 12 codes for deferred comp, HSA, etc.
4. **Verify investment income** — Tie 1099-INT, 1099-DIV, and Schedule B. Verify 1099-B transactions on Schedule D / Form 8949.
5. **Verify retirement income** — Tie 1099-R distributions to Line 4 or 5. Verify taxable amount and any rollover exclusions.
6. **Verify pass-through income** — Tie each K-1 to the appropriate schedule (E, F, etc.). For each pass-through entity reporting a loss:
   - **Basis limitation**: Does the taxpayer have sufficient basis to absorb the loss? If no basis worksheet is provided and a loss is claimed, this is a hard stop — flag as requiring basis documentation.
   - **At-risk limitation**: Is Form 6198 present? If losses are claimed from an activity, at-risk must be addressed.
   - **Passive activity**: Is Form 8582 present? Flag any pass-through loss flowing through without Form 8582 when the taxpayer has W-2 income (suggesting they may not materially participate).
   - **QBI deduction**: Verify the Section 199A computation. Flag if income is from a specified service trade or business (SSTB) above the income threshold without a phase-out calculation.
7. **Verify deductions and credits** — Check Schedule A itemized deductions or standard deduction. Verify credits (child tax, EV, education, etc.) against supporting forms.
8. **Verify withholding and estimated payments** — Tie federal withholding to all W-2s and 1099s. Verify estimated tax payments against IRS records if available.
9. **Summarize findings** — Produce a severity-graded findings list (see Output Format).
10. **Audit risk assessment** — Note 1-3 items that present elevated audit risk. State facts: "This item may draw scrutiny because [specific reason]." This is not a risk score — it is a factual assessment of areas most likely to draw IRS attention.

## Control Points

- **Material variance** — Any discrepancy above the firm's materiality threshold requires preparer review and correction before filing.
- **Missing source documents** — Do not mark the review complete if source docs are missing for reported income.
- **Pass-through loss without basis** — A loss claimed without a basis worksheet is a hard stop requiring documentation before the review can continue.

## Red Flags

- Reported income doesn't match any source document on file
- K-1 shows a large loss but no basis worksheet is present
- Withholding on return exceeds withholding on source documents
- Prior-year carryforwards present but no supporting schedule
- QBI deduction taken without a supporting computation
- Pass-through loss claimed without basis documentation or Form 6198
- Passive loss allowed without Form 8582 or evidence of material participation
- QBI deduction taken on SSTB income above threshold without phase-out calculation
- Large ISO exercise, accelerated depreciation, or preference items present — verify Form 6251 is present and AMT computation is correct
- Cross-return coordination needed: K-1 amounts from a related 1120-S, 1065, or 1041 should tie to the issuing entity's return

## Output Format

A structured findings report with severity-graded issues:

```
Issue #[X] — [HIGH / MEDIUM / LOW]
Line/Schedule: [specific form reference]
Finding: [what was found]
Amount: $[X] (X% of gross income)
Correction: [recommended action]
Authority: [IRC §, Reg., or procedure if applicable]
```

Organized into sections:
- **Confirmed** — Line items that tie to source documents
- **Issues** — Severity-graded findings (HIGH / MEDIUM / LOW)
- **Missing Support** — Items where source docs are absent
- **Preparer Questions** — Items requiring judgment or additional facts
- **Audit Risk Items** — 1-3 items with factual risk assessment

## Safety Constraints

- Do not mark the return as reviewed-complete if material variances or missing documents remain.
- Do not draft a response to an IRS notice based on this review without preparer confirmation.
- Do not characterize audit risk as a probability or percentage. Professional judgment on acceptable risk levels belongs to the signing partner.
