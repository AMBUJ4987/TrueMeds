import pandas as pd

# -----------------------------
# Load raw master CSV
# -----------------------------
df = pd.read_csv("CSV/master.csv")

# -----------------------------
# Helper function
# -----------------------------
def merge_columns(cols):
    """Merge multiple similar columns into one."""
    existing = [c for c in cols if c in df.columns]

    if not existing:
        return pd.Series([None] * len(df))

    return df[existing].bfill(axis=1).iloc[:, 0]


# -----------------------------
# Create clean dataframe
# -----------------------------
clean = pd.DataFrame()

clean["Serial_No"] = merge_columns([
    "S.No",
    "S.No.",
    "S. No."
])

clean["Drug_Name"] = merge_columns([
    "Product/Drug Name",
    "Name of Drugs/medical device/cosmetics"
])

clean["Batch_No"] = merge_columns([
    "Batch No."
])

clean["Manufacturing_Date"] = merge_columns([
    "Manufacturing Date",
    "Manufact uring Date",
    "Manufactu ring Date",
    "Manufacturi ng Date",
    "Date of Manufacture",
    "Date of Manufa - cture"
])

clean["Expiry_Date"] = merge_columns([
    "Expiry Date",
    "Date of Expiry"
])

clean["Manufacturer"] = merge_columns([
    "Manufactured By",
    "Manufactured by"
])

clean["Failure_Reason"] = merge_columns([
    "NSQ Result",
    "Reason for failure"
])

clean["Laboratory"] = merge_columns([
    "Reported by CDSCO Laboratory",
    "Reported by State Laboratory"
])

clean["Drawn_By"] = merge_columns([
    "Drawn By"
])

clean["Remarks"] = merge_columns([
    "Remarks"
])

clean["Status"] = df["Status"]

clean["Source"] = df["Source"]

clean["Document"] = df["Document"]

# -----------------------------
# Remove empty rows
# -----------------------------
clean.dropna(
    subset=["Drug_Name", "Batch_No"],
    how="all",
    inplace=True
)

# -----------------------------
# Remove duplicates
# -----------------------------
clean.drop_duplicates(inplace=True)

# -----------------------------
# Reset index
# -----------------------------
clean.reset_index(drop=True, inplace=True)

# -----------------------------
# Save
# -----------------------------
clean.to_csv("CSV/master_clean.csv", index=False)

print("=" * 40)
print("Cleaning Complete")
print(f"Rows : {len(clean)}")
print("Saved : CSV/master_clean.csv")
print("=" * 40)