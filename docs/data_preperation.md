# 📊 Data Cleanup & Preperation Summary
This document describes the preparation steps for the synthetic dataset (`data/synthetic_profiles.csv`), which is used for testing and prototyping only. It is not intended for final model training or evaluation.

---

## 📝 Purpose of the Synthetic Dataset
- Serve as a sandbox for validating the preprocessing pipeline.
- Enable UI testing without requiring access to sensitive or real data.
- Provide structure for transitioning to real-world datasets.

---  
## 🔢 1. Numerical Feature Validation

| Feature   | Rule                         | Purpose                               |
|-----------|------------------------------|----------------------------------------|
| `age`     | Clipped to [18, 100]         | Ensure adult and valid human range     |
| `income`  | Clipped to [15,000, 250,000] | Remove unrealistic income values       |
| `expenses`| Clipped to [500, 15,000]     | Ensure reasonable monthly spending     |

```python
df['age'] = df['age'].clip(18, 100)
df['income'] = df['income'].clip(15_000, 250_000)
df['expenses'] = df['expenses'].clip(500, 15_000)
```

## 🔤 2. Categorical Feature Rules
Standardize string casing and remove whitespace to ensure consistency across entries.
```python
df['investment_knowledge'] = df['investment_knowledge'].str.lower().str.strip()
df['financial_goal'] = df['financial_goal'].str.lower().str.strip()
df['risk_tolerance'] = df['risk_tolerance'].str.lower().str.strip()
```

## 🧮 3. Derived Feature: savings_ratio
Computed as : 
```python
savings_ratio = 1 - (12 * expenses) / income
``` 
This represents the proportion of income saved annually.
No clipping is applied to allow for negative values (deficit behavior).
```python
df['savings_ratio'] = 1 - (df['expenses'] * 12) / df['income']
```

## 🚩 4. Flag Feature: is_deficit
Boolean column add to indecate overspending behavior.
```python
df['is_deficit'] = df['savings_ratio'] < 0
```
This captures users who spand more then they earn in a year.

✅ Final Columns (Post-Preparation)

| Column | Description|
|--------|------------|
|   age  | Clean integer [18-90]|
|income|Cleaned float [$15k-$250k]|
|expences|Cleaned float [$500-$15k]|
|investment_knowledge|Standardized categorical|
|financial_goal|Standardized categorical|
|risk_tolerance| Target label|
|savings_ratio|Derived float; may be negative|
|is_deficit|Boolean flag for overspanding|

---

## ⚠️ Notes
- This dataset is fully synthetic and randomly generated.
-	It does not reflect real financial behavior.
-	When real data is introduced, additional steps will be required:
-	Handling missing values and nulls
-	Outlier detection and treatment
-	Categorical imputation
-	Type coercion and validation