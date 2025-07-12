import pandas as pd
import numpy as np
from pathlib import Path

def load_and_preper_data(file_path:Path = Path("data/synthetic_profiles.csv")) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"❌ File not found: {file_path.resolve()}")
    
    df = pd.read_csv(file_path)

    # Data cleanups
    df.dropna(inplace=True)
    df["age"].clip(18,90)
    df["income"].clip(15_000,250_000)
    df["expences"].clip(500,15_000)

    # Normalization 
    df["investment_knowledge"] = df["investment_knowledge"].str.lower().str.strip()
    df["financial_goal"] = df["financial_goal"].str.lower().str.strip()
    df["risk_tolerance"] = df["risk_tolerance"].str.lower().str.strip()

    # Derived feature
    df["savings_ratio"] = 1 - (df["expences"] * 12) / df["income"]
    df["is_deficit"] = df["savings_ratio"] < 0

    # Categorical validation
    valid_knowledge = {'none', 'basic', 'advanced'}
    valid_goal = {'short-term', 'long-term'}
    valid_risk = {'low', 'medium', 'high'}

    assert df['investment_knowledge'].isin(valid_knowledge).all()
    assert df['financial_goal'].isin(valid_goal).all()
    assert df['risk_tolerance'].isin(valid_risk).all()

    return df


df = pd.read_csv("data/financial_risk_assessment.csv")

print(df[df.isnull().any(axis=1)])