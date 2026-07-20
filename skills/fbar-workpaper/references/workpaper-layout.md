# FBAR Workpaper Layout — Sheet Specs & Extraction Detail

Read this when building the workbook (Phase 4) or extracting from scanned statements
(Phase 2). SKILL.md carries the workflow, gates, and judgment; this file is the
column-by-column reference so you don't have to hold it in context the whole time.

Apply `firm-stack:excel-report-format` standards throughout. FBAR-specific overrides:
open-items rows use a peach fill (#FDE8D8) to distinguish them from standard flagged
items; section headers use navy (#2B4770).

---

## Extracting from scanned statements (Phase 2)

Foreign bank statements are almost always scanned PDFs. Convert to images for
vision-based extraction:

```python
import fitz, os
doc = fitz.open(os.path.expanduser("~/path/to/statement.pdf"))
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    pix.save(os.path.expanduser(f"~/path/to/statement_p{i+1}.png"))
```

Extract per account using targeted vision queries:

- **Cover / account opening page:** account holder name, address, account number,
  bank name, branch, SWIFT/BIC, country
- **Balance pages:** year-end balance, maximum balance during the year (if shown),
  monthly average balances, sub-account detail
- **Tax certificate:** gross income by category, foreign tax withheld, field codes,
  tax year, currency

---

## Sheet 1 — FBAR Summary

- Taxpayer info block: name, TIN, filing type, tax year, report date
- Accounts table — one row per account:

| Column | Content |
|---|---|
| A | Account # (as it appears at the institution) |
| B | Bank / Financial Institution |
| C | Country |
| D | Currency |
| E | Maximum Value (foreign currency) |
| F | Treasury FMS Year-End Rate |
| G | Maximum Value (USD) — formula: `=E*F` |
| H | Account Type (Bank Deposit / Securities / Other) |
| I | Ownership / Signatory |
| J | Status / Notes |

- Total aggregate USD value row — `=SUM()` of column G
- Threshold note: aggregate >$10,000 USD at any point during the year triggers filing
- Filing instructions block: BSA E-Filing URL, due date, extension mechanics

---

## Sheet 2 — Account Detail

One section per account. Each section contains:

- **Section A — Institution Master:** Bank name, address, SWIFT/BIC, branch, account number
- **Section B — Year-End Balances:** Balance in native currency, exchange rate, USD equivalent
- **Section C — Sub-Account / Deposit Detail** (if applicable):

| Column | Content |
|---|---|
| A | Deposit / Sub-Account # |
| B | Currency |
| C | Opening Balance |
| D | Deposit Date |
| E | Maturity Date |
| F | Nominal Rate |
| G | Effective Rate |
| H | Rate Type (Fixed / Variable) |
| I | Balance at Year-End |

- **Section D — Annual Averages:** Monthly average balance from bank statement
  (used to assess whether maximum balance may have been higher than year-end)

---

## Sheet 3 — Interest Income (Schedule B / Form 1116)

- Source document reference (certificate number, issue date)

| Column | Content |
|---|---|
| A | Income Category |
| B | Amount (Foreign Currency) |
| C | IRS Annual Average Rate |
| D | Amount (USD) — formula: `=B*C` |
| E | Notes |

Rows to include (as applicable):
- Taxable interest income
- Tax-exempt interest (note treaty basis if applicable)
- Foreign tax withheld
- Net income after withholding — formula

- U.S. reporting treatment note: exempt from foreign tax ≠ exempt from U.S.
  Schedule B reporting
- Form 1116 note: passive basket, foreign tax credit available for withheld amounts

---

## Sheet 4 — Open Items Checklist

Standard open items (always include, mark resolved or pending):

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Maximum balance confirmation — obtain if only year-end balance available | | |
| 2 | IRS annual average exchange rate — confirm official rate for income conversion | | |
| 3 | Treasury FMS year-end rate — confirm official rate for balance conversion | | |
| 4 | Sub-account FBAR treatment — do sub-deposit numbers = separate FBAR accounts? | | |
| 5 | Form 8938 (FATCA) assessment — threshold analysis vs. filing status | | |
| 6 | Foreign residency / treaty status confirmation | | |
| 7 | FBAR filing via BSA E-Filing System — client signature required | | |
| 8 | Schedule B Part III — confirm "Yes" to foreign account question | | |
| 9 | Form 1116 — foreign tax credit, passive basket | | |
