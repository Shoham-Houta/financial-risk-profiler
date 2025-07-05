import pandas as pd
import numpy as np
import os

np.random.seed(42)

n: int = 500

ages: int = np.random.randint(20,65,n)
incomes: float = np.random.normal(75000,20000,n).clip(30000,150000)
expences: float = np.random.normal(3500,1000,n).clip(1500,8000)
invesment_knowledge: str = np.random.choice(["none","basic","advanced"],size=n,p=[0.3,0.5,0.2])
financial_goals: str  = np.random.choice(["short-term","long-term"],size=n,p=[0.4,0.6]) 

def assign_risk(row):
    if row["investment_knowledge"] == "advanced" and row["income"] > 90000:
        return "high"
    elif row["investment_knowledge"] == "none" and row['income'] < 40000:
        return "low"
    else:
        return "medium"
    

df = pd.DataFrame(
    {
        "age": ages,
        "income": incomes,
        "expences": expences,
        "investment_knowledge": invesment_knowledge,
        "financial_goal": financial_goals,
    }
)

df["risk_tolerance"] = df.apply(assign_risk,axis=1)

os.makedirs("data",exist_ok=True)
df.to_csv("data/synthetic_profiles.csv",index=False)

print("✅ Dataset generated and saved to data/synthetic_profiles.csv")