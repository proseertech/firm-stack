# Initial-Return Checklist (Year 1 and New Clients)

**This file is an internal procedures manual.** Use the checks below to decide what to test, then report results in the findings table. **Do not quote or paste this file to the user.**

Run when the Initial Return box (Item E) is checked, the filing history shows year 1, or this is a new client whose prior returns the firm did not prepare. Many first-year positions are made by *how the first return is filed* rather than by a separate statement — and several are irrevocable. Confirm each decision was deliberate, that the return reflects it, and that a statement is present **only where one is required**.

Terminology follows the Terminology section of `SKILL.md`.

## Entity classification and structure

**Goal: confirm the entity is properly a C corporation for this year and that the classification evidence is in the file.**

Checks:

1. **Form 8832** — If the entity is an LLC or other eligible entity electing corporate treatment, confirm Form 8832 was filed **and accepted**, and that the effective date matches the return's start date. The acceptance letter is the evidence; the filed form alone is not. If an intended election was missed, flag late-election relief for the preparer rather than papering over it.
2. **Hard stop** — A missing Form 8832 acceptance where corporate classification depends on it. Do not treat the return as review-complete.
3. **Header data** — Legal name, EIN (matches the CP 575 notice), address, and business activity code. Confirm the incorporation date and the date the corporation began business, which can differ and which drive the amortization start months below.
4. **Consolidated group** — If this is the first consolidated year, confirm **Form 851** is attached and a **Form 1122** consent is present for each new member. A consolidated return filed without them is defective.
5. **Controlled group** — Identify membership now. It governs the §448(c) gross-receipts aggregation, §163(j), the shared §179 dollar limit, CAMT AFSI aggregation, and the §1561 accumulated earnings credit. A year-1 return that tests any of these standalone sets the wrong pattern for every later year.

## Tax year and accounting method

**Goal: confirm the year end and the method were permissible choices, since the first return is the election.**

Checks:

1. **Tax year** — Confirm the year end selected is permissible, and that any business-purpose fiscal year is supported (a Form 1128 ruling where required). Confirm short-period mechanics if the first year is short: proration and annualization for estimates, and short-year depreciation.
2. **Accounting method** — The method box *is* the election. Confirm cash vs. accrual is permissible under §448 — a C corporation above the §448(c) gross-receipts threshold on an aggregated basis, and certain entities regardless of size, cannot use the cash method. No Form 3115 is needed now, but the wrong box adopts a method that later requires one.
3. **Method consistency** — The method box, the books, and the M-1/M-3 explanation must describe the same thing.
4. **Inventory** — If inventories exist: confirm the method adopted, that **Form 1125-A** is attached, and that UNICAP/§263A was addressed or the small-business exemption documented. **LIFO requires Form 970** filed with this return.

## Start-up, organizational, and stock-issuance costs

**Goal: confirm the three-way classification and the amortization mechanics. Do not look for a §195 or §248 election statement — the regulations deem the election made by return treatment.**

Checks:

1. **Three-way classification** — Every pre-operating and formation cost lands in exactly one bucket. A single "start-up and organizational costs" line with no split is a finding.
   - **§195 start-up** — Investigatory and pre-opening operating costs of the trade or business.
   - **§248 organizational** — Costs incident to the creation of the corporation, chargeable to capital account, and of a character that would be amortized over a limited life: incorporation and state filing fees, organizational meeting costs, temporary-director expenses, and the legal and accounting fees of organizing.
   - **Stock-issuance and capital-raising costs** — Costs of issuing or selling stock, printing certificates, underwriting and placement fees, registration fees, and the legal and accounting fees attributable to the offering. These are **capital costs that reduce paid-in capital**: not deductible, not amortizable, no 180-month schedule. Amortized stock-issuance costs are a **[HIGH]** finding, and they are routinely swept into the §248 bucket.
2. **§195 mechanics** — Up to $5,000 deducted, reduced dollar-for-dollar to the extent start-up expenditures exceed $50,000; the remainder amortized over 180 months beginning with the month the **active trade or business begins**. **Deemed elected** under Reg. §1.195-1(b); no statement is required, and a missing statement is not a finding.
3. **§248 mechanics** — Up to $5,000 deducted, same $50,000 phase-down; the remainder amortized over 180 months beginning with the month the **corporation begins business**. **Deemed elected** under Reg. §1.248-1(c); no statement is required.
4. **Confirm on the return** — The $5,000 (as limited) and the 180-month amortization actually appear, and each schedule starts in **its own** correct month. Incorporation date, business-start date, and the date the active trade or business begins can all differ; a schedule keyed to the incorporation date, or defaulted to January of the first year, is a finding.
5. **Capitalization is a decision** — Forgoing the deemed election and capitalizing is **irrevocable** and applies to **all** costs in that category. If the return capitalizes, confirm it was deliberate and documented; if it looks like a data-entry default, flag it while the return is still amendable in the year of election.

## Election statements — confirm attached where required

**Goal: distinguish the elections that genuinely require a statement or form from the deemed elections above. Absence here is a finding.**

Checks:

- **Form 8832** classification acceptance (above) — the controlling evidence
- **§179** — Form 4562, Part I; check the limit, the phase-out, and the controlled-group sharing rule
- **De minimis safe harbor** (Reg. §1.263(a)-1(f)) — annual election statement if the fixed-asset policy relies on it
- **Bonus depreciation elect-out** (§168(k)(7)) — statement by class; silence means bonus applies
- **§163(j)(7)(B) electing real property trade or business** — common in year 1 for real estate corporations and **irrevocable**; it requires ADS for nonresidential real property, residential rental property, and QIP. Confirm the first-year fixed-asset register was actually set up on ADS, because a later correction is a method change
- **§174A** capitalize-and-amortize election, if domestic R&E is being capitalized rather than expensed
- **LIFO** — Form 970 with this return
- **§266** carrying-charge capitalization and **Reg. §1.263(a)-3(n)** repair-capitalization elections — annual statements
- **§453(d)** installment-method elect-out — statement with a timely return
- **Form 1128** — if a non-calendar year requires a ruling

## Opening balances and estimated tax

**Goal: confirm the return starts from zero, or from a documented predecessor.**

Checks:

1. **Schedule L beginning column** — Should be zero or blank for a true first year. A populated beginning balance means either a predecessor entity or a wrongly checked Initial Return box — either way, a finding. If a predecessor exists (incorporation of a going business, a §351 transfer, a conversion), confirm the carryover basis and paid-in capital are documented rather than imported from the books.
2. **No carryovers** — No NOL, capital loss, charitable, credit, or §163(j) carryforwards should appear on a first return. Any carryover is a finding requiring an explanation.
3. **Retained earnings and E&P** — Beginning retained earnings on Schedule L and M-2 start at zero absent a documented predecessor. Establish the E&P tracking schedule now; E&P drives distribution characterization for the life of the corporation and is the hardest thing to reconstruct later.
4. **Estimated tax** — First-year corporations have **no prior-year safe harbor**. Confirm current-year estimates were computed on projected liability, that Form 2220 exposure was tested, and that the client is enrolled in EFTPS. A first-year return with no estimates and a balance due usually carries a penalty the software did not compute.

## First-year consistency checks

**Goal: catch the year-1 mechanics that set patterns for every later return.**

Checks:

1. **Depreciation conventions** — First-year placed-in-service dates drive the convention; run the mid-quarter test (more than 40% of additions in the fourth quarter). Year 1 is when the register's conventions get locked in.
2. **Bonus depreciation rate** — Matched to each asset's **acquisition** date for 2025 additions (40% before January 20, 2025; 100% on or after), including assets acquired under a pre-January 20 written binding contract.
3. **Officer compensation** — Confirm officers are on payroll from the point services began, and that **Form 1125-E** is attached at total receipts of $500,000 or more.
4. **Schedule K walk** — Answer every question rather than leaving defaults: accounting method, affiliation and controlled-group membership, 20%/50% ownership in both directions, foreign ownership at 25% or more with the matching Form 5472 count, and the §163(j) small-business questions.
5. **Foreign triggers from inception** — A first-year corporation with foreign owners, subsidiaries, or accounts has the same automatic per-form penalties as a mature one. Run the international presence check in `corporate-verification-procedures.md`.
6. **State registrations and first-year state filings** — Match the operating footprint; route to Preparer Questions per the federal-only scope constraint, and to `nexus-screen` if the footprint looks multistate.
