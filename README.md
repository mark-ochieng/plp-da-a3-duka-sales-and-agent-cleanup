# PLP Data Analytics Assignment 3: Duka Sales and Agent Data Cleanup

**Author:** John Mark Ochieng  
**Cohort:** 1 Million Devs  
**Specialization:** Data Analytics with Python

## Project Overview

This repository contains two data analytics engagements completed using Python, pandas and NumPy.

### Engagement 1: Duka Electronics Sales Analysis

The first engagement explores sales transactions for Duka Electronics across five branches between January and June 2026. The analysis investigates branch performance, product revenue, sales channels, weekend versus weekday performance and monthly revenue trends. It also includes an Excel branch revenue summary and an exported dataset of Premium Online orders from Nairobi and Mombasa.

### Engagement 2: Mobile Money Agent Network Data Cleaning

The second engagement audits and cleans a mobile-money transaction dataset. It addresses duplicate records, inconsistent transaction types, missing amounts, date formatting problems, suspicious outliers and unknown agent IDs. A reusable Python cleaning module performs the cleaning, merges transactions with the agent register and generates county-level and weekly summaries.

## Repository Structure

```text
plp-da-a3-duka-sales-and-agent-cleanup/
│
├── README.md
├── generate_data.py
├── cleaning_pipeline.py
├── requirements.txt
│
├── duka_sales_exploration.ipynb
├── agent_cleanup.ipynb
│
├── excel/
│   └── duka_branch_summary.xlsx
│
└── outputs/
    ├── premium_online_coast_capital.csv
    └── agent_transactions_clean.csv
```

## Requirements

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

The project uses:
- pandas
- numpy

## Dataset Generation

Both engagements use reproducible synthetic datasets generated using fixed random seeds.

Run the following command from the repository root:

```bash
python generate_data.py
```

The generator creates:

| Dataset | Description | Rows |
|---|---|---:|
| duka_sales.csv | Duka Electronics sales | 1,000 |
| agents.csv | Mobile-money agent register | 20 |
| agent_transactions.csv | Raw mobile-money transactions | 612 |

The generated raw CSV files are not committed to the repository. They can be recreated using the generator.

## Running the Notebooks

The notebooks can be opened and executed using Google Colab or Jupyter Notebook.

### 1. Duka Electronics

Open `duka_sales_exploration.ipynb`.

Run the notebook from top to bottom after generating the datasets.

The analysis covers:
- Initial data inspection and quality checks.
- Derived columns and price-band classification.
- Branch revenue and order rankings.
- Product revenue and units sold.
- Weekend and weekday performance.
- Monthly revenue comparisons.
- Premium Online orders from Nairobi and Mombasa.
- Excel summary validation.

### 2. Mobile Money Agent Network

Open `agent_cleanup.ipynb`.

After generating the datasets, run the notebook from top to bottom.

The notebook imports `clean_agent_data()` from `cleaning_pipeline.py` and performs:
- Data-quality auditing.
- Duplicate removal and transaction type standardisation.
- Missing amount imputation.
- IQR outlier detection.
- Date standardisation.
- Agent register merging and validation.
- County and weekly transaction summaries.
- Data Quality Reporting and privacy considerations.

## Duka Electronics Executive Summary

- Duka Electronics recorded **1,000 orders** across five branches between January and June 2026.
- Nairobi was the leading branch, generating **KES 26,106,100** from 376 orders.
- Laptops generated the highest product revenue at **KES 41,535,000**, while tablets led in units sold with 691 units.
- Weekday orders accounted for **723 orders**, generating KES 51,856,200, compared with 277 weekend orders generating KES 19,936,300.
- April was the best-performing month with **KES 13,518,300**, while June was the weakest with KES 10,903,400.

## Agent Data Cleaning: Before and After

| Validation measure | Before cleaning | After cleaning |
|---|---:|---:|
| Transaction rows | 612 | 600 |
| Duplicate transaction IDs | 12 | 0 |
| Missing transaction amounts | 22 | 0 |
| Unknown agent references | 8 | 7 |
| Unique transaction IDs | 600 | 600 |

The cleaning pipeline removed 12 duplicate records and retained 600 unique transactions. Twenty missing amounts remaining after duplicate removal were imputed using the median of KES 1,776.50.

Forty suspicious transaction amounts were flagged using the IQR method, with an upper threshold of KES 6,044.25. These transactions were retained for investigation rather than automatically deleted.

Seven transactions referencing unknown agent AG099 were preserved, with their county values left missing.

The total cleaned transaction value was KES 2,688,427.

## Output Files

- `excel/duka_branch_summary.xlsx`: Branch revenue calculations, region lookup and revenue PivotTable.
- `outputs/premium_online_coast_capital.csv`: Premium Online orders from Nairobi and Mombasa.
- `outputs/agent_transactions_clean.csv`: Cleaned mobile-money transactions with quality flags and agent county information.

## Reproducibility and Data Governance

The datasets are synthetic and generated using fixed random seeds. The cleaning pipeline is reusable and records its actions in a cleaning log. Potential outliers and unknown agents are retained and flagged to support investigation and prevent unnecessary data loss.

The project also considers privacy principles under the Kenya Data Protection Act, 2019, including data minimisation, restricted access, secure storage and protection of personal information.
