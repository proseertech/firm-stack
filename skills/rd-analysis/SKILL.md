---
name: rd-analysis
version: 1.2.0
description: |
  Screen a business client for R&D tax credit (Section 41) study candidacy — before
  quoting a study fee or promising credits. Analyzes the client's activities against the
  four-part test, estimates qualified research expenses and the credit, checks whether the
  client can actually use it, and returns a Strong / Possible / Not-recommended call with
  an ROI estimate. Use this whenever someone is weighing an R&D study: "should we do an
  R&D credit study for this client", "does this manufacturer qualify for the research
  credit", "is the dev shop a good R&D candidate", "can they use the credit", "what would
  an R&D study get them" — even when they don't say "Section 41" or "screening". This is
  the candidacy screen. It can also organize source evidence for a study in preparation.
allowed-tools:
- Read
- Write
- AskUserQuestion
- WebFetch
when-to-use: |
  "R&D credit", "R&D study", "research credit", "research and development tax credit",
  "should we do an R&D study", "does this client qualify for the R&D credit",
  "R&D candidate", "is this an R&D candidate", "Section 41", "§41 credit",
  "qualified research", "four-part test", "R&D analysis", "R&D screening",
  "payroll tax offset", "can they use the research credit"
metadata:
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
- For study preparation, use **Evidence intake** to build a reviewable working register.
  The responsible tax professional determines eligibility, substantiation, and the filed credit.
- Verify time-sensitive rules against the applicable year's [Form 6765 and instructions](https://www.irs.gov/forms-pubs/about-form-6765).
  Use official source URLs without including client data. Ask for the applicable
  instructions or route to `tax-advisor` when the sources are unavailable.
  Use [IRC §41](https://uscode.house.gov/us/usc/119-136/t26/s41/),
  [Treas. Reg. §1.41-4](https://www.ecfr.gov/current/title-26/section-1.41-4) and
  [Treas. Reg. §1.41-2](https://www.ecfr.gov/current/title-26/section-1.41-2)
  for eligibility and expense rules. Route unresolved questions to `tax-advisor`.

## Required Inputs

Start with the records available. Identify missing facts and which conclusions they block.
Gather the following before estimating a usable credit:

- Tax year, taxpayer, entity type, tax profile, related entities, and any predecessors
- Candidate business components, intended use, technical work, and where it occurred
- Current-year wages or other qualifying compensation, supported time allocations,
  supplies, eligible computer rental, and contract research records
- QREs separately for each of the three prior tax years, including confirmed zeros,
  and any prior credit claims or elections
- For a payroll-offset screen, current-year gross receipts, earliest tax year with gross
  receipts, and any prior payroll elections. Include controlled-group and predecessor facts.
- For a regular-credit comparison, the preceding four years' receipts and the applicable
  fixed-base history. For the Section G small-claim exception, obtain the prior three years'
  average receipts and the controlled group's current QREs.

## Workflow

1. **Screen by business component.** Identify the new or improved function, performance,
   reliability, or quality. Record the uncertainty at the outset about capability, method,
   or design, the hard-science or engineering principles used, and the alternatives and
   experiments used to resolve it. Apply the substantially-all test using the regulatory
   80% threshold measured on cost or another consistently applied reasonable basis.
   Apply the domestic R&E requirement for the relevant tax year. Check exclusions for
   routine quality control, adaptation, duplication, post-commercial-production work,
   funded research, and foreign research.
   For software, establish the intended users and functions at the outset. Flag internal
   general and administrative software for the high-threshold-of-innovation test.
   Check for innovation, significant economic risk arising from technical uncertainty,
   and whether commercially available software could serve the intended use without
   modifications that themselves meet the innovation and risk tests. Separate third-party
   and dual-function uses for review under §1.41-4(c)(6).

2. **Estimate qualified research expenses (QREs).** Separate wages for performing, directly
   supervising, and directly supporting qualified research. Use the statutory wage basis,
   including qualifying self-employment income where applicable, and supported time
   allocations. Apply the full-wage rule separately for each employee when at least 80%
   of their wages are allocable to qualified services. Separately record qualifying
   supplies and eligible off-premises computer rental. For contracts, use 65% of the
   documented eligible spend in the ordinary case. Check that
   the agreement was in place before the work, the taxpayer has rights to the results and
   bears the expense even if research fails, and the services and work locations qualify.
   Allocate mixed invoices by activity and place prepaid costs in the year of performance.

3. **Estimate the credit.** For the ordinary QRE portion of ASC, use 14% of the positive
   excess of current-year QREs over half of the preceding three tax years' average QREs
   if each prior year had QREs. Use 6% of current-year QREs if any one prior year had
   confirmed zero QREs. Missing records or a year with no prior claim do not establish a
   zero. Use consistent QRE definitions and verify controlled-group and short-year rules.
   For the ordinary QRE portion of the regular method, use 20% of the positive excess of
   current-year QREs over the greater of half of current-year QREs or the applicable
   fixed-base percentage times average gross receipts for the prior four tax years.
   For tax years beginning after 2024, compare the full credit with its corresponding
   reduction of §174A domestic research expenditures against a timely
   [§280C(c) election](https://uscode.house.gov/us/usc/119-136/t26/s280C/) for the
   reduced credit (currently 79% of the full credit). Route election and transition
   analysis to `tax-advisor`.

4. **Assess ability to use the credit.** Evaluate general business credit limits, any
   pass-through owner limits, and carryback or carryforward where relevant. For a
   §41(h) payroll election, check that current-year gross receipts are below $5 million and
   that there were no gross receipts before the five-tax-year period ending in the claim
   year. Apply aggregation, predecessor rules, and the five-election limit. Check the
   timely election, available employer payroll liability, and applicable limits, including
   the $500,000 annual cap. Report estimated utilization separately from the credit.

5. **Check documentation scope.** For tax years beginning after 2025, check whether Form
   6765 Section G is required. Its current exceptions cover a qualified small business
   making the payroll election, or an original return with group QREs of at most $1.5
   million and prior-three-year average gross receipts of at most $50 million under the
   form's rules. When required, follow the instructions for the 80%/top-50 component
   schedule and remaining aggregate. Apply the amended-claim requirements separately.

6. **Produce the recommendation.** Weigh estimated usable credit against a sourced study
   fee or range. State which inputs and assumptions support the result. Return Strong,
   Possible, or Not-recommended. When inputs are missing, leave the affected estimates
   open and label any illustrative amounts with their assumptions.

## Evidence intake

For a request to prepare a study, organize available records before asking for missing data:

- **Business components and evidence.** Record the product or process, tax year, intended
  use, improvement, initial uncertainty, alternatives tested, observed results, dates,
  and source links. Identify hypotheses, acceptance plans, and results separately. Treat
  a repository as a source and map related repositories to the appropriate components.
- **People, hours, and wages.** Record the person, employer, location, activity, component,
  total and activity hours for the same period, wage basis, allocation method, and
  supporting records. Distinguish development, direct supervision, direct support, user
  acceptance, and routine QA. Use GitHub activity as corroboration, with separate time and
  payroll support. Identify automation or shared accounts before assigning human work.
- **Contractors and other costs.** Record payer, vendor, statement of work, invoice and
  ledger references, dates and locations of work, linked activities, and substantiated
  allocation. Separate wages, supplies, computing, and contractor amounts.
- **Review status.** Distinguish observed evidence, participant recollection, and open
  questions. Leave unverified hours, wages, allocation percentages, and costs blank.
  Report what period and sources the working register covers.

## Control Points

Stop and get a human decision before recommending a study when:

- **Activities don't clearly clear the four-part test.** Don't recommend a study built on
  activities that plainly fail — overstated R&D claims are an IRS scrutiny magnet, and an
  audit that unwinds the credit costs the client far more than the study fee.
- **Utilization or research allocation is unverified.** Confirm available tax or payroll
  liability, employer and payer, and the support for material cost allocations before
  treating the estimate as usable.

## Red Flags

Pause and surface these before landing on a recommendation:

- Business is primarily services with no technical development activity.
- Activities consist of routine operations, standard implementation, or ordinary QA.
- A history of NOLs or other credit limits may defer utilization. Check the carry rules
  and payroll election eligibility.
- Prior-year returns claimed the credit aggressively — review for consistency, since an
  inconsistent or overstated history raises audit exposure.

## Output Format

Candidate screening summary:
- Activity assessment by business component with evidence and unresolved facts
- Estimated QREs by category and credit by supported method
- Estimated utilization, study cost, and ROI where inputs support them
- Strong / Possible / Not-recommended with reasoning and next steps

For evidence intake, deliver the business-component, people/time, and expense registers
with linked records, gaps, and review status.

## Safety Constraints

- This is a screening estimate, not a formal R&D study. Do not present the output as
  documentation sufficient to support an R&D credit claim on a filed return.
- Keep borderline work and unsupported amounts out of the supported subtotal and route
  unresolved eligibility or filing judgments to the responsible tax professional.
- Keep client records within approved sources and destinations. Obtain authorization before
  transferring private records to a study platform or another third party.
