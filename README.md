# Invoice Tax Workbench / 發票核算助手

發票核算助手是一個給會計師、記帳士、事務所助理與小型企業財務人員使用的發票整理原型。它的核心目標是減少人工使用計算機反覆加總、拆稅、核對金額，再手動整理到 Excel 的時間。

This project is a lightweight invoice tax workbench for accounting workflows. It helps users enter invoice amounts, automatically split business tax, classify corporate income tax expense categories, validate totals, and export clean spreadsheet-ready data.

## Live Usage

The main app is a single HTML file:

- `index.html`

You can open it directly in a browser. No server, install step, or framework is required.

## Colab Usage

This repo also includes Google Colab-ready versions:

- `invoice-workbench-colab.ipynb`  
  Upload this notebook to Google Colab and run the first two cells.

- `invoice-workbench-colab-onecell.py`  
  Copy the whole file into one Colab cell and run it.

- `invoice-workbench-colab-cells.txt`  
  A split-cell version for manual copy and paste.

## Why This Exists

The project came from observing a real accounting workflow:

1. Accountants often receive many invoices or receipts from clients.
2. They repeatedly check gross amount, net sales amount, and 5% business tax.
3. They also need to separate business tax handling from corporate income tax expense classification.
4. Existing workflows often jump between paper invoices, calculators, Excel, and manual notes.

This tool keeps the first version focused: enter or paste invoice data, automatically calculate, verify, classify, and export.

## Key Features

- Gross amount to net sales amount and 5% business tax split
- Net sales amount to business tax and gross amount calculation
- Per-row calculation mode:
  - Gross amount auto split
  - Net sales amount auto calculate
  - Manual verification
- Difference check: `sales amount + tax amount = gross amount`
- Business tax fields:
  - Tax type
  - Deductible / non-deductible / pending
  - Deductible business tax total
- Corporate income tax fields:
  - Expense category
  - Recognition status
  - Recognized expense amount total
- Copy table for Excel
- Download CSV
- Download Excel-compatible `.xls`
- Auxiliary calculator, collapsed by default

## Business Tax vs Corporate Income Tax

The tool intentionally separates two tax concepts:

### Business Tax

Business tax is handled at the invoice row level. The tool helps calculate 5% tax and whether the tax can be deducted.

Example:

```text
Gross amount: 525
Sales amount: 500
Business tax: 25
```

### Corporate Income Tax

Corporate income tax is not calculated as a direct tax amount per invoice. Instead, the tool helps classify whether an expense can be recognized and under which expense category.

Example fields:

- Office supplies
- Travel
- Transportation
- Rent
- Utilities
- Entertainment
- Fixed assets
- Other expenses

## Demo Cases

### Gross Amount Auto Split

Input:

```text
Gross amount = 525
```

Output:

```text
Sales amount = 500
Tax amount = 25
Check = matched
```

### Net Amount Auto Calculate

Input:

```text
Sales amount = 1000
```

Output:

```text
Tax amount = 50
Gross amount = 1050
Check = matched
```

## Key Algorithms

The core logic is intentionally small and easy to explain.

```js
const net = Math.round(gross / 1.05);
const tax = gross - net;
const expectedTax = Math.round(net * 0.05);
const diff = net + tax - gross;
const isCredit = taxType === "應稅" && deductible === "可扣抵";
```

These lines cover the main accounting workflow:

- Reverse-calculate sales amount from gross amount
- Calculate tax from sales amount
- Validate row totals
- Determine deductible business tax

## File Structure

```text
.
├── index.html
├── invoice-workbench-colab.ipynb
├── invoice-workbench-colab-onecell.py
├── invoice-workbench-colab-cells.txt
├── LICENSE
└── README.md
```

## Target Users

- Accountants
- Bookkeepers
- Accounting firm assistants
- Small business finance staff
- Students demonstrating AI-assisted workflow automation

## Prompt Engineering Notes

This project also demonstrates an AI-assisted product development process:

- Start from real observation instead of abstract feature ideas
- Correct the initial AI assumption that the calculator should be the main feature
- Shift the workflow toward automatic calculation
- Separate business tax from corporate income tax after user feedback
- Keep AI as a coding and prototyping assistant, not as a tax decision maker

## Limitations

- This is a prototype, not certified tax software.
- It does not replace professional accounting judgment.
- OCR and QR code invoice scanning are not included yet.
- Exported `.xls` is Excel-compatible XML, not a full modern `.xlsx` package.
- Tax rules and accounting treatment should be reviewed by qualified professionals.

## Future Improvements

- OCR for paper invoices
- QR code reading for Taiwan electronic invoices
- Batch upload
- Client profile management
- Expense category prediction
- LLM-assisted memo generation
- Modern `.xlsx` export
- GitHub Pages deployment

## License

MIT License.
