import pandas as pd

df = pd.read_csv("CSV/master_clean.csv")

risk_map = {
    "Spurious": "High",
    "NSQ": "Medium",
    "Revised Alert": "Medium",
    "Unknown": "Review Required"
}

df["Risk_Level"] = df["Status"].map(risk_map)

# If Status is blank (NaN)
df["Risk_Level"] = df["Risk_Level"].fillna("Review Required")

df.to_csv("CSV/master_clean.csv", index=False)

print("Risk_Level column added successfully.")