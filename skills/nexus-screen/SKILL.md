---
name: nexus-screen
version: 1.0.0
description: |
  Screen a business client for state tax nexus exposure — income/franchise and
  sales/use — across every state where it has customers, people, or property.
  Runs the AICPA-style nexus questionnaire against data the firm already has
  (sales by state, payroll by state, inventory/3PL locations, org and
  registration states) and produces a state-by-state exposure matrix with
  "further examination needed" flags, a P.L. 86-272 activity analysis, and
  prioritized next steps. Use this whenever someone asks where a client owes
  filings: "do we have nexus in Texas", "the client hired a remote employee in
  another state", "they sell on Amazon — where do they need to register", "state
  tax exposure review", "do they need to file in other states" — even if they
  never say the word "nexus." This is an exposure screen, not a nexus study or
  legal conclusion.
trigger: |
  "nexus", "nexus screen", "state tax nexus", "do we have nexus", "economic nexus",
  "state tax exposure", "where does the client need to file", "do they need to register",
  "remote employee in another state", "sales tax registration", "P.L. 86-272",
  "86-272", "marketplace facilitator", "Amazon FBA state tax", "trailing nexus",
  "voluntary disclosure", "which states"
allowed-tools:
  - Read
  - Write
  - Bash
  - AskUserQuestion
tier: power-user
---

# Nexus Screen: State Tax Exposure Screening

## Purpose

Identify the states where a business client likely has — or is at risk of having — income/franchise or sales/use tax filing obligations, before a state finds the client first. The screen runs each state in the client's footprint through the standard nexus questionnaire dimensions (physical presence, economic thresholds, employee and representative activities, internet/marketplace activities, affiliate relationships) and grades the exposure. A "yes" on any dimension does not mean nexus exists — it means further examination is needed, and the output says so explicitly, state by state.

This is a screening tool in the same family as `costseg-analysis` and `rd-analysis`: it produces a prioritized exposure map and next steps, not a nexus determination, a registration filing, or a legal opinion.

## Scope & Handoffs

- **Screen, not study** — per-state statutory research, exposure quantification (back-tax estimates, penalty/interest), and voluntary disclosure agreement (VDA) strategy → `tax-advisor`.
- **Client-facing explanation** of the exposure map or a recommendation memo → `tax-memo` or `client-email`.
- Local-jurisdiction taxes (city/county) are out of scope; note in the output that states flagged for nexus may also carry local obligations.

## Required Inputs

Ask for what's missing rather than screening around it — a nexus screen that silently omits the payroll or inventory dimension produces false comfort in exactly the states most likely to assess.

- **Sales by state** — gross receipts and transaction counts, current year plus three prior years (the economic-nexus data grid; from the GL, e-commerce platform, or sales tax software)
- **Payroll by state** — employee locations, including remote employees and any terminated remote arrangements; traveling employee/rep activity descriptions
- **Property and inventory locations** — owned/leased offices, warehouses, equipment, consigned stock, and third-party fulfillment inventory (for Amazon FBA, request the inventory-location report — states obtain this data from Amazon)
- **Entity facts** — state of organization, states where registered/qualified with the secretary of state, states where returns are currently or previously filed, affiliate structure
- **Pass-through investments** — K-1s from entities operating or owning property in other states (flow-through nexus)
- **Sales channels** — direct website, marketplace facilitators (Amazon, Etsy…), in-state affiliates/referral arrangements, licensing of software or intangibles, digital products/streaming

## Workflow

1. **Build the candidate-state list** — Union of: every state with sales, every state with an employee or property, the organization state, states with pass-through activity, and states with 3PL/FBA inventory. Do not screen only the states the client asks about; the exposure is usually in the state nobody mentioned.
2. **Screen each candidate state across five dimensions:**
   - **Physical presence** — office/warehouse/business location, owned or leased property or equipment, inventory (including consigned stock and fulfillment-center inventory), resident or remote employees, employees using in-state homes for business (address, inventory storage, records). Physical presence generally creates both income/franchise and sales/use nexus and is not protected by economic-threshold safe harbors.
   - **Economic nexus** — compare the state's sales and transaction counts against that state's current economic-nexus thresholds for sales/use tax (and factor-presence thresholds for income/franchise where the state has them). Do not hardcode thresholds — they vary by state and change; verify the current-year threshold for each flagged state, and check all years in the data grid, not just the current one (crossing a threshold in a prior year starts the obligation then).
   - **Employee/representative activities vs. P.L. 86-272** — for income tax only: solicitation of orders for sales of **tangible personal property** (and ancillary pre-sale activities) is federally protected. Parse the client's actual in-state activities against the unprotected list: order approval, collections, repairs/installation/technical assistance, repossession, credit investigations, training/seminars, maintaining displays beyond short periods, managerial/research activities, non-TPP sales (services, software, digital goods get **no** 86-272 protection). Note the MTC's 2021 revised statement: many states now treat interactive website/app features (chat support, post-sale assistance via the site, market-research cookies) as unprotected in-state activity — flag internet-heavy sellers even where physical activities look protected. **86-272 never protects sales/use tax, franchise taxes on net worth, or gross-receipts taxes** (e.g., WA B&O, OH CAT, TX franchise) — say so per state where relevant.
   - **Internet/marketplace activities** — marketplace-facilitator sales (facilitator usually collects sales tax, but the client's own-site sales still count toward thresholds, and some states still require seller registration), click-through/affiliate referral arrangements, in-state servers, software licensed for in-state use, digital products and streaming, extended warranties sold online.
   - **Affiliate and flow-through nexus** — commonly owned entities with in-state presence; K-1 interests in partnerships operating or owning property in the state.
3. **Check registration and filing posture** — For each state flagged, compare against where the client is actually registered and filing. The dangerous quadrant is *flagged + never filed*: no return means no statute of limitations, so the lookback is open-ended.
4. **Check trailing nexus** — For states where the client previously had nexus but facts changed (closed office, terminated remote employee), note that many states assert nexus for a trailing period; flag rather than conclude.
5. **Grade and prioritize** — Per state, per tax type (income/franchise vs. sales/use): **Likely exposure** (physical presence or clearly crossed thresholds, not filing), **Needs examination** (threshold-adjacent, 86-272 position doing heavy lifting, marketplace-mix questions), **Monitor** (approaching thresholds), or **No indicators**. Rank by revenue at stake and years of non-filing.
6. **Recommend next steps** — Per priority state: current-year registration, VDA consideration (flag — the VDA decision and negotiation belong to the signing partner and `tax-advisor`), prospective compliance, or continued monitoring with the specific threshold to watch.

## Control Points

Stop and route to the signing partner — these are judgment or strategy calls, not screening outputs:

- **Never conclude nexus.** The deliverable flags exposure and says "further examination needed"; whether nexus exists in a specific state is a professional judgment made against that state's current law.
- **VDA and lookback strategy** — Approaching a state (or deciding not to) changes the client's legal posture. Present the exposure; do not recommend contacting a state without partner sign-off.
- **86-272-dependent positions** — Where the income-tax answer turns entirely on 86-272 protection for an internet-active seller, flag it as unsettled (MTC revised statement, ongoing litigation) and hand the position analysis to `tax-advisor`.

## Red Flags

Pause and surface to the user when:

- Amazon FBA or other 3PL inventory in states with no registration — physical-presence nexus the client doesn't know it has, and states actively mine fulfillment data
- Remote employees hired post-2020 in states with no payroll registration or filings
- Years of sales above common threshold levels in a state with no returns ever filed — open-ended lookback
- The client sells services, SaaS, or digital goods and is relying on 86-272 — the protection only covers tangible personal property
- A pass-through K-1 showing in-state property or apportionment for a state the owner has never filed in
- Gross-receipts-tax states (WA, OH, TX, OR, NV…) in the footprint being analyzed only through an income-tax lens
- Sales data that only exists for the current year — economic nexus is tested year by year; request the historical grid

## Output Format

A state-by-state exposure matrix plus prioritized findings:

| State | Income/Franchise | Sales/Use | Driver | Registered? | Filing? | Priority |
|-------|------------------|-----------|--------|-------------|---------|----------|
| TX | Needs examination (franchise — no 86-272 protection) | Likely exposure | FBA inventory + $X sales | No | No | 1 |

Followed by:

- **Per-state detail** for every non-"No indicators" state: the specific facts that triggered the flag, which dimension(s), the years affected, and what further examination would resolve it
- **P.L. 86-272 activity analysis** — protected vs. unprotected activities identified, and where the MTC internet-activity position could change the answer
- **Recommended next steps** — ranked, with VDA candidates flagged for partner decision
- **Data gaps** — inputs not provided and which states' answers they could change

Every flag carries the caveat the AICPA checklist itself uses: a "yes" answer means further examination is likely necessary, not that nexus exists.

## Safety Constraints

- Do not conclude that nexus exists or does not exist in any state — flag and grade exposure only; the determination belongs to the signing partner against current state law.
- Do not hardcode economic-nexus thresholds, factor-presence amounts, or state tax rates — they vary by state and change frequently; verify current figures for each flagged state before they appear in the output.
- Do not estimate back-tax dollar exposure in the screen — quantification requires state-specific rate, apportionment, and penalty research (`tax-advisor`).
- Do not contact, register with, or draft submissions to any state agency from this screen.
- State the screen's data boundaries in the deliverable: it covers the states and years for which data was provided, income/franchise and sales/use taxes only, and excludes local-jurisdiction taxes.
