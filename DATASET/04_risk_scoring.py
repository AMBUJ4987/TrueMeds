import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("CSV/master_clean.csv")

# -----------------------------
# Normalize Status using filename
# -----------------------------
for index, row in df.iterrows():

    filename = str(row["Document"]).lower()

    status = row["Status"]

    # If blank, unknown, or review required, classify again
    if pd.isna(status) or str(status).strip() in ["", "Unknown", "Review Required"]:

        if "spurious" in filename:
            status = "Spurious"

        elif "state" in filename or "stnsq" in filename:
            status = "NSQ"

        elif "nsq" in filename or "nosq" in filename:
            status = "NSQ"

        elif "revise" in filename:
            status = "Revised Alert"

        else:
            status = "Review Required"

        df.at[index, "Status"] = status

# -----------------------------
# Risk Mapping
# -----------------------------
risk_map = {
    "Spurious": "High",
    "NSQ": "Moderate",
    "Revised Alert": "Moderate",
    "Review Required": "Review Required"
}

df["Risk_Level"] = df["Status"].map(risk_map)
df["Risk_Level"] = df["Risk_Level"].fillna("Review Required")

# -----------------------------
# Remove old Record_ID if present
# -----------------------------
if "Record_ID" in df.columns:
    df.drop(columns=["Record_ID"], inplace=True)

# -----------------------------
# Remove duplicates
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Reset Index
# -----------------------------
df.reset_index(drop=True, inplace=True)

# -----------------------------
# Create Record_ID
# -----------------------------
df.insert(0, "Record_ID", range(1, len(df) + 1))

# -----------------------------
# Save
# -----------------------------
df.to_csv("CSV/master_final.csv", index=False)

# -----------------------------
# Summary
# -----------------------------
print("=" * 55)
print("Dataset Finalized Successfully")
print("=" * 55)

print(f"\nTotal Records : {len(df)}")

print("\nStatus Distribution")
print(df["Status"].value_counts())

print("\nRisk Distribution")
print(df["Risk_Level"].value_counts())

print("\nSaved as : CSV/master_final.csv")

print("=" * 55)