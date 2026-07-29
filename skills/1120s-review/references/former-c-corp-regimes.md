# Former-C-Corporation Regimes

Detailed procedures for workflow step 11. **Conditional — run only when the corporation was previously a C corporation, or acquired assets with a carryover basis from a C corporation in a transaction described in §1374(d)(8).** If neither is true, say so in the deliverable rather than leaving the step silently unaddressed.

These three regimes share a trigger and a failure mode: they are entity-level taxes and terminating events that a clean trial-balance tie-out will never surface, and they are usually missed years after the conversion, when the supporting facts are hardest to reconstruct.

Terminology and box-code conventions follow the Terminology section of `SKILL.md`.

**Posture.** Verify that the analysis exists, that its inputs match the return, and that its output flows through correctly. **Do not compute NUBIG, the §1374 tax, or the §1375 tax from scratch** — these require conversion-date valuations and a full asset history, and a partial recomputation produces a confident wrong number.

## 1. Built-in gains tax (§1374)

### When it applies

- The corporation has a **net unrealized built-in gain (NUBIG)** at the S-election date — the aggregate excess of fair market value over adjusted basis in its assets — and disposes of an asset within the **five-year recognition period**.
- **§1374(d)(8)** creates a separate recognition period and NUBIG for assets acquired from a C corporation in a carryover-basis transaction. A corporation that has always been an S corporation can still owe BIG tax this way; screen acquisitions, not just conversion history.

### What to check

- **The conversion-date schedule exists.** Asset-by-asset fair market value and adjusted basis as of the election date, supporting the NUBIG figure. Absent that schedule, no BIG position on the return is verifiable — record it as Missing Support and a **[HIGH]** finding rather than clearing asset sales.
- **Recognition-period arithmetic.** Confirm the disposition date falls inside the five-year window measured from the first day of the first S year. A sale one day outside the window is a very different return.
- **Recognized built-in gain identified for each disposition.** Gain is built-in only to the extent it existed at conversion; post-conversion appreciation is not subject to §1374. A disposition treated as entirely built-in gain, or entirely not, both warrant the workpaper.
- **The three limitations were applied** — the pre-limitation amount, the taxable-income limitation (the tax cannot exceed what a C corporation would owe on the same income), and the overall NUBIG limitation, with any amount limited out carried forward within the recognition period.
- **Offsets** — C-corporation NOL and capital loss carryforwards and certain credits can reduce the §1374 base even though they cannot offset pass-through income. Confirm they were applied here rather than swept into the S return.
- **Flow-through of the tax.** The §1374 tax is an entity-level liability, and under §1366(f)(2) it **reduces the amount of the recognized built-in gain that passes through to shareholders**. Confirm the reduction appears on Schedule K and the K-1s; a return that pays the tax and also passes the full gain through double-taxes the shareholders.
- **Non-sale triggers.** Collections on a cash-basis receivable existing at conversion, completion of long-term contracts, and inventory turnover under LIFO/FIFO differences can all produce recognized built-in gain without an asset sale. Screen these where the conversion is recent.

## 2. Accumulated E&P and distribution ordering

### What to check

- **Opening AE&P ties to the final C-corporation return** and is disclosed on Schedule B. AE&P survives the S election indefinitely; it does not decay.
- **Distribution ordering** — AAA → PTI → **AE&P (taxable dividend)** → OAA → remaining stock basis → capital gain. Detail in `basis-and-distributions.md` §2.
- **Forms 1099-DIV issued** for the AE&P portion. A distribution beyond AAA with AE&P present and no 1099-DIV is a hard-stop control point: the shareholders' income is understated and an information return is missing.
- **Ordering elections** — the §1368(e)(3) election to distribute AE&P first and the deemed-dividend election each require a statement with shareholder consents. Both are legitimate planning tools, often used deliberately to clear AE&P and escape the §1375 exposure below. Confirm the statement exists rather than inferring the election from the numbers.
- **AE&P movement** — AE&P changes only for actual dividend distributions, redemptions, and the §1375 tax. It is not affected by S-year operating income or losses. Unexplained AE&P movement means someone treated it as a book account.

## 3. Excess passive investment income (§1375) and termination

### The two-part trigger

Both conditions must hold in the same year:

1. **Passive investment income exceeds 25% of gross receipts** — royalties, rents, dividends, interest, and annuities, with the statutory adjustments (rents are excluded where significant services are provided; gross receipts from sales of stock or securities count only to the extent of gains).
2. **The corporation has AE&P at the end of the year.**

### What to check

- **The computation exists** where passive receipts look material. Compute the ratio as a screen from Schedule K and page 1, but treat the classification of rents and the gross-receipts adjustments as the preparer's call — a **[MEDIUM]** "Preparer to analyze" row where it is close.
- **The tax** — imposed at the highest corporate rate on **excess net passive income**, limited to the corporation's taxable income computed as if it were a C corporation. Confirm the workpaper applies the limitation.
- **Flow-through effect** — the §1375 tax reduces the passive investment income passed through to shareholders. Confirm the K-1s reflect it.
- **Termination risk — three consecutive years.** Under §1362(d)(3) the election terminates on the first day of the year following the third consecutive year of excess passive investment income with AE&P. **Check the two prior years, not just this one.** A third-year return that pays the §1375 tax and says nothing about termination is a **[HIGH]** finding: the election is ending and the client needs to know before the next year begins.
- **The planning point belongs in Preparer Questions** — distributing AE&P (or making the §1368(e)(3) election) eliminates the §1375 exposure and the termination risk going forward. Flag it; do not model it.

## 4. LIFO recapture (§1363(d))

- A C corporation using LIFO that elects S status must include the **LIFO recapture amount** — the excess of FIFO over LIFO inventory value — in income on its **final C-corporation return**.
- The resulting tax is payable in **four equal annual installments**, the first with the final C return and the remainder with the next three S-corporation returns.
- **What to check:** for a conversion within the last four years, confirm the recapture was reported, the installment schedule is in the file, and this year's installment is being paid with the return. A missed installment is a collection matter that surfaces as a notice, not as a return error.
- Confirm the basis of the inventory was increased by the recapture amount — otherwise the same income is taxed again as the inventory turns.

## 5. Inadvertent termination

- If any check above (or the eligibility and one-class-of-stock tests in workflow steps 1 and 2) indicates the election terminated, **§1362(f) relief is a private letter ruling request, not a return position.** Flag it for the preparer with the specific defect and its date.
- Do not file, or clear, a return as an S corporation on the assumption that relief will be granted. Note the exposure and route the decision to the signing partner.
