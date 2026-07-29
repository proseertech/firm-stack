# Shareholder Basis, Distributions, and the AAA/OAA Accounts

Detailed procedures for workflow steps 7 and 9. These are the checks the trial-balance reconciliation cannot see: a return can tie perfectly and still allow a loss that isn't there, report a taxable distribution as tax-free, or corrupt the account balances that determine next year's answer.

Terminology and box-code conventions follow the Terminology section of `SKILL.md`.

**Scope of the entity-level review.** Stock basis, debt basis, and the taxability of a distribution are ultimately determined on the *shareholder's* return, on Form 7203. The corporation's obligation — and what this review tests — is whether the return and the K-1s furnish accurate, correctly classified inputs, and whether the entity-level accounts (AAA, OAA, PTI, AE&P) are maintained correctly. Report missing or misclassified inputs as findings; do not present a shareholder-level conclusion as the corporation's.

## 1. Stock and debt basis

### The two pools

- **Stock basis** and **debt basis** are separate pools under §1367. Losses reduce stock basis first, then debt basis. Distributions reduce **stock basis only** — a distribution can never be absorbed by debt basis.
- **Entity-level liabilities are not basis.** Corporate borrowing gives no shareholder any basis. This is the sharpest difference from partnership mechanics and the most common error when a preparer or a software conversion carries over a 1065 model. If the basis workpaper shows a "share of liabilities" line, the schedule is built wrong.
- **Debt basis requires bona fide indebtedness running directly from the shareholder to the corporation** (Reg. §1.1366-2(a)(2)). A **guarantee** of third-party debt creates no basis until the shareholder actually makes payment. Back-to-back and related-entity loans can work, but only with the notes, the money trail, and terms consistent with real debt — confirm all three are in the file before accepting debt basis that supports a loss.

### Annual ordering (§1367, §1368, §1366(d))

Apply in this order; the sequence changes the answer:

1. **Increase** stock basis for income items — including tax-exempt income and the excess of depletion deductions over basis.
2. **Decrease** for distributions (stock basis only), limited to zero.
3. **Decrease** for nondeductible, non-capital expenses.
4. **Decrease** for deductible losses and deductions.

- Steps 3 and 4 may be reversed under the **Reg. §1.1367-1(g) election**, which lets losses come first. The election binds later years and requires a statement — confirm it exists before accepting an ordering that assumes it.
- **Distributions come before losses.** A shareholder with just enough basis for either a distribution or a loss gets the distribution tax-free and the loss suspended, not the other way around. A workpaper that nets them or takes the loss first overstates the deduction.
- **Loss limitation and carryforward** — Loss and deduction in excess of stock plus debt basis is disallowed and carried forward indefinitely under §1366(d)(2), pro-rata across categories (Reg. §1.1366-2(a)(4)) rather than absorbed by whichever item the preparer prefers.
- **Basis restoration** — Later net increases restore **debt basis first**, up to the amount previously reduced, before stock basis (Reg. §1.1367-2(c)). A loan repaid while debt basis is still reduced produces gain to the shareholder — check repayments against the reduced-basis history.
- **Post-termination transition period** — Suspended losses may be used against basis during the PTTP under §1366(d)(3). If the election terminated, confirm the PTTP treatment is documented rather than assumed.

### What to check on the return

- A loss on any K-1 with no basis worksheet in the file: **hard stop**, and a Missing Support item.
- Basis schedules that begin with a prior-year ending figure that doesn't match last year's return.
- Debt basis appearing in the same year the shareholder guaranteed a bank loan, with no payment by the shareholder.
- Distributions and losses in the same year with no evidence of the ordering above.
- Whether the corporation furnished each shareholder the data needed for Form 7203 — required with the 1040 when the shareholder claims a loss, receives a non-dividend distribution, disposes of stock, or receives a loan repayment.

## 2. Distributions and §1368 ordering

Test **every** distribution, not just the annual total that rolled through Schedule M-2.

### Ordering when there is no AE&P

1. Tax-free to the extent of **stock basis** (§1368(b)(1)).
2. The excess is gain from the sale or exchange of stock (§1368(b)(2)) — capital, and generally long-term if the stock was held more than a year.

### Ordering when AE&P exists

Apply in sequence: **AAA → PTI → AE&P → OAA → remaining stock basis → capital gain.**

- The AAA portion is tax-free to the extent of stock basis, then gain.
- The **AE&P portion is a taxable dividend** requiring Forms 1099-DIV. A distribution beyond AAA with AE&P present and no 1099-DIV issued is a hard-stop control point — the shareholders' income is understated and an information return is missing.
- Two elections can change the ordering, each requiring a statement with shareholder consents: the **§1368(e)(3) election to distribute AE&P first**, and the **deemed-dividend election**. Do not infer either from the numbers; find the statement.

### Other distribution checks

- **Property distributions** — The corporation recognizes gain under §311(b) as if the property were sold at fair market value. Loss is **not** recognized. Confirm the gain is on the return and flows through Schedule K by character.
- **Non-pro-rata distributions** — Coordinate with workflow step 2. They do not by themselves create a second class of stock, but they require an explanation: a governing provision conferring different rights, or payments that are actually compensation, loans, reimbursements, or a redemption.
- **Redemptions** — Confirm the treatment (sale/exchange vs. §301 distribution) and the AAA and AE&P effects, and that the stock ledger and Item J-equivalent percentages reflect the change for per-share-per-day purposes.
- **Timing** — Distributions are tested against basis and the accounts as of the year end, but per-share-per-day allocation and mid-year ownership changes affect who received what. Tie the distribution detail by shareholder and date to the stock ledger.
- **Consistency** — Total distributions must agree across Schedule K line 16d, Schedule M-2, the Schedule L equity movement, and the shareholder distribution detail. A figure that appears in one and not the others is a finding regardless of which is right.

## 3. AAA, OAA, PTI, and Schedule M-2

- **AAA (§1368(e)(1))** — The running tally of S-year taxable income and deductions, increased by separately stated income and page 1 income, decreased by losses, deductions, nondeductible non-capital expenses, and distributions.
- **AAA adjustment ordering (Reg. §1.1368-2(a))** — A **net positive** adjustment for the year is applied **before** distributions; a **net negative** adjustment is applied **after**. Getting this backwards changes how much of a distribution is tax-free.
- **AAA can go negative from losses, never from distributions** (Reg. §1.1368-2(a)(3)(ii)). Distributions reduce AAA only to zero. A negative ending AAA driven by distributions is an error to correct, not a balance to carry forward — and it will misstate every future distribution.
- **OAA** — Tax-exempt income and the nondeductible expenses related to it. Tax-exempt income posted to AAA inflates the tax-free distribution capacity and is one of the most persistent errors in S-corp files because nothing else on the return contradicts it.
- **PTI** — Pre-1983 previously taxed income. Rare, but if a column exists it must be preserved rather than netted away; it sits ahead of AE&P in the ordering.
- **AE&P** — Not an M-2 column on the current form, but it must be tracked and is disclosed on Schedule B. Tie it to the final C-corporation return and confirm it only changes for actual dividend distributions, §1375 tax, and redemptions.
- **PTET** — An entity-level PTET deduction reduces AAA. Confirm it is booked, and that the ordering interaction with AE&P was considered where AE&P exists.
- **Reconciliation** — Beginning AAA/OAA/PTI to the prior-year return; ending balances to the current-year activity; total distributions to Schedule K line 16d.
