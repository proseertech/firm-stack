---
name: rd-analysis
version: 1.1.0
description: |
  Screen a business client for R&D tax credit (Section 41) study candidacy — before
  quoting a study fee or promising credits. Analyzes the client's activities against the
  four-part test, estimates qualified research expenses and the credit, checks whether the
  client can actually use it, and returns a Strong / Possible / Not-recommended call with
  an ROI estimate. Use this whenever someone is weighing an R&D study: "should we do an
  R&D credit study for this client", "does this manufacturer qualify for the research
  credit", "is the dev shop a good R&D candidate", "can they use the credit", "what would
  an R&D study get them" — even when they don't say "Section 41" or "screening". This is
  the candidacy screen, not the study itself and not open-ended tax research.
trigger: |
  "R&D credit", "R&D study", "research credit", "research and development tax credit",
  "should we do an R&D study", "does this client qualify for the R&D credit",
  "R&D candidate", "is this an R&D candidate", "Section 41", "§41 credit",
  "qualified research", "four-part test", "R&D analysis", "R&D screening",
  "payroll tax offset", "can they use the research credit"
allowed-tools:
  - Read
  - Write
  - AskUserQuestion
tier: power-user
---

# R&D Analysis: Research & Development Tax Credit Candidate Screening

## Purpose

Decide whether a client is a strong enough candidate for a Section 41 R&D tax credit study
to be worth recommending — before the firm quotes a study fee or the client hears the word
"credit." The credit rewards businesses that conduct qualified research activities (QRAs);
some small businesses can take it as a payroll-tax offset even when they owe no income tax.
The output is a go / maybe / no candidacy call with the numbers behind it, not the study.

This is a screening tool. It sizes the opportunity and flags disqualifiers so the firm
doesn't sell a study that yields immaterial or unusable credits — or, worse, an aggressive
claim that draws IRS scrutiny.

## Scope & Handoffs

- Open-ended R&D technical questions (e.g. "is this specific activity a QRA under the
  regs", §174/§174A capitalization treatment) → **`tax-advisor`**.
- This skill screens candidacy. It does not produce the study, the QRE substantiation, or
  a defensible credit computation.

## Required Inputs

Ask for anything missing before screening — a credit estimate built on guessed wages or the
wrong entity type sends the firm into a study that doesn't pay off.

- Business description and primary activities (what they build/improve, and how)
- Industry
- Entity type (C-corp, S-corp, partnership) and tax profile
- Approximate annual W-2 wages for employees doing technical work
- Annual spend on supplies or contract research tied to technical activities
- Whether the company has previously claimed the R&D credit
- Gross receipts for the past 5 years (needed for the alternative simplified credit base)

## Workflow

1. **Screen activities against the four-part test.** Each qualified research activity must
   clear all four prongs:
   - **Permitted purpose** — a new or improved product, process, software, technique,
     formula, or invention
   - **Technological uncertainty** — it was not known in advance how to achieve the goal
   - **Process of experimentation** — testing alternatives to eliminate the uncertainty
   - **Technological in nature** — relies on engineering, physical/biological science,
     computer science, or similar

   Call out activities that plainly fail (routine quality control, market research,
   management studies, social-science research, cosmetic/style changes) — these can't
   anchor a study.

2. **Estimate qualified research expenses (QREs).** Wages for time spent on QRAs, supply
   costs consumed in research, and 65% of contract research costs.

3. **Estimate the credit.** Use the alternative simplified credit (ASC) method:
   14% × (current-year QREs − 50% of average QREs for the prior 3 years). If the client had
   no QREs in any of the three prior years, the ASC rate is 6% of current-year QREs instead.
   Note the regular method if it produces a materially better result for this client.
   Flag the §280C interaction: a client claiming the credit must either reduce its §174/§174A
   research deduction by the credit or elect the reduced credit under §280C(c). With domestic
   R&E expensing restored for 2025 (§174A), confirm which election fits — route the detailed
   analysis to `tax-advisor`.

4. **Assess ability to use the credit.** C-corps offset tax directly. Pass-throughs
   (S-corp, partnership) flow the credit to owners, who need enough tax liability to absorb
   it. Startups can elect the payroll-tax offset — available to companies ≤5 years old with
   ≤$5M in gross receipts — which turns the credit into cash even with no income tax owed.

5. **Estimate study cost.** R&D credit studies typically run $5,000–$25,000+ depending on
   complexity and the number of employees interviewed.

6. **Produce the recommendation.** Weigh estimated usable credit against study cost and
   return Strong / Possible / Not-recommended with the reasoning.

## Control Points

Stop and get a human decision before recommending a study when:

- **Activities don't clearly clear the four-part test.** Don't recommend a study built on
  activities that plainly fail — overstated R&D claims are an IRS scrutiny magnet, and an
  audit that unwinds the credit costs the client far more than the study fee.
- **Pass-through owners may not be able to use the credit.** For S-corps and partnerships,
  confirm the owners have enough tax liability to absorb the credit before recommending —
  a credit that flows to owners who can't use it is not a reason to buy a study.

## Red Flags

Pause and surface these before landing on a recommendation:

- Business is primarily services with no technical development activity.
- The described "R&D" is really routine operations or incremental tweaks to existing
  processes — it won't survive the four-part test.
- History of NOLs — the credit may be unusable unless the payroll-tax offset election
  applies (small startups only; see Workflow step 4).
- Prior-year returns claimed the credit aggressively — review for consistency, since an
  inconsistent or overstated history raises audit exposure.

## Output Format

Candidate screening summary:
- Activity assessment against the four-part test (which activities qualify, which don't, why)
- Estimated QREs, broken into wages / supplies / contract research
- Estimated credit amount (ASC method; note regular method if materially better)
- Ability-to-use assessment (entity type, owner liability, payroll-offset eligibility)
- Estimated study cost range
- Estimated ROI (usable credit vs. study cost)
- Recommendation: Strong / Possible / Not-recommended
- Caveats and next steps

## Safety Constraints

- This is a screening estimate, not a formal R&D study. Do not present the output as
  documentation sufficient to support an R&D credit claim on a filed return.
- Flag borderline qualifiers rather than counting them as clean QREs — they need specialist
  review before any credit is claimed.
