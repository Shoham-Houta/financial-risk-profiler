
# 📊 Data Preparation Summary for Financial Risk Profiling

## ✅ 1. Core Column Selection
Selected features from the dataset:
- Age
- Gender
- Education Level
- Marital Status
- Income
- Credit Score
- Loan Amount
- Loan Purpose
- Employment Status
- Years at Current Job
- Payment History
- Debt-to-Income Ratio
- Number of Dependents
- Previous Defaults
- Marital Status Change

---

## ✅ 2. Missing Value Handling

| Column                   | Strategy            |
|--------------------------|---------------------|
| Income, Credit Score | Impute with median |
|Loan amount| Impute with median base on purpose or 0 if no loan history exist|
| Number of Dependents, Previous Defaults | Impute with 0 |
| Years at Current Job     | Impute with median |
| DTI Ratio                | Impute as Loan Amount / Income |
| Categorical columns      | Impute with mode or "Unknown" |

---

## ✅ 3. Derived Features

### 🔹 Debt & Expense Estimation
- `Annual_Debt` = `DTI` × `Income`
- `Estimated_Expenses` = `Income × 0.80 × (1 + 0.10 × Number of Dependents)`
- `Estimated_Savings` = `Income − Estimated_Expenses`
- `Non_Debt_Expenses` = `Estimated_Expenses − Annual_Debt`
- `Savings_Ratio` = `Estimated_Savings / Income`
- `Implied_Debt_From_Spending` = `max(0, Estimated_Expenses − Income)`

### 🔹 Loan-Related Calculations
- `Loan_to_Income_Ratio` = `Loan Amount / Income`
- `Loan Purpose` → encoded as categorical risk
- `Credit Score` → binned into buckets
- (Optional) `Estimated_Monthly_Payment` via annuity formula

---

## ✅ 4. Feature Engineering & Normalization
- One-hot encode: Gender, Education Level, Marital Status, Loan Purpose, Employment Status, Payment History
- Ordinal/binning: Credit Score, Years at Current Job (optional)
- Normalize: Income, Loan Amount, Annual Debt, Savings Ratio, etc.

---

## ✅ 5. Optional Risk Indicators
- `Total_Burden` = `Annual_Debt + Implied_Debt_From_Spending`
- `At_Risk` flags:
  - Savings Ratio < 0.05
  - Loan-to-Income Ratio > 0.5
  - Credit Score < 600
  - Dependents > 2 with low income
