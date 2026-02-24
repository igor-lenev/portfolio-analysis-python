## 📊 Sample Chart
# portfolio-analysis-python
Financial portfolio analysis using Python (Pandas, Matplotlib)
# 📊 Portfolio Analysis with Python

## 📌 Project Overview
This project analyzes a financial investment portfolio using Python.

It calculates:
- Profit per asset
- Return %
- Portfolio allocation
- Total portfolio return

## 🛠 Technologies Used
- Python
- Pandas
- Matplotlib
- OpenPyXL

## 📈 Features
- Automatic profit calculation
- Return % calculation
- Portfolio performance summary
- Visualization export (PNG chart)

## ▶ How to Run

1. Install dependencies:

2. Run:

## 📊 Example Output

Total portfolio return: X%

Bar chart showing asset performance.

---

👤 Author: Igor Lenev  
Aspiring Data Analyst | Automation & Financial Analytics
# Save sorted report
portfolio_sorted = portfolio.sort_values("Return_%", ascending=False)

with pd.ExcelWriter("portfolio_report.xlsx", engine="openpyxl") as writer:
    portfolio_sorted.to_excel(writer, index=False)

print("Excel report saved successfully.")
