import re
import pandas as pd
from rapidfuzz import process, fuzz

# Load the CDSCO dataset
master_df = pd.read_csv(
    r"E:\TrueMeds\DATASET\CSV\master_final.csv"
)

medicine_names = (
    master_df["Drug_Name"]
    .fillna("")
    .astype(str)
    .tolist()
)

MATCH_THRESHOLD = 75


# Normalize medicine names
def normalize_name(name):

    name = str(name).lower()

    words_to_remove = [
        "tablets",
        "tablet",
        "capsules",
        "capsule",
        "ip",
        "usp",
        "bp",
        "mg",
        "ml",
        "injection",
        "oral",
        "solution",
        "suspension"
    ]

    for word in words_to_remove:
        name = name.replace(word, "")

    name = re.sub(r"\d+", "", name)
    name = re.sub(r"[^a-z ]", "", name)

    return " ".join(name.split())


# Normalize manufacturer names
def normalize_company(company):

    if pd.isna(company):
        return ""

    company = str(company).lower()

    remove = [
        "m/s",
        "private",
        "pvt",
        "pvt.",
        "limited",
        "ltd",
        "ltd.",
        "pharmaceuticals",
        "pharma",
        "&"
    ]

    for word in remove:
        company = company.replace(word, "")

    company = re.sub(r"[^a-z ]", "", company)

    return " ".join(company.split())


# Match medicine using:
# 1. Drug name
# 2. Manufacturer
# 3. Batch number
def find_match(fields):

    if not fields:
        return None

    drug_name = fields.get("drug_name", "")
    manufacturer = fields.get("manufacturer", "")
    batch_number = fields.get("batch_number", "")

    normalized_query = normalize_name(drug_name)

    normalized_database = [
        normalize_name(name)
        for name in medicine_names
    ]

    # Retrieve Top 10 candidates using medicine name
    candidates = process.extract(
        normalized_query,
        normalized_database,
        scorer=fuzz.token_sort_ratio,
        limit=10
    )

    if not candidates:
        return None

    best_score = -1
    best_row = None

    best_drug_score = 0
    best_company_score = 0
    best_batch_score = 0

    for candidate in candidates:

        drug_score = candidate[1]

        # Ignore weak medicine-name matches
        if drug_score < 80:
            continue

        index = candidate[2]
        row = master_df.iloc[index]

        company_score = fuzz.token_sort_ratio(
            normalize_company(manufacturer),
            normalize_company(row["Manufacturer"])
        )

        batch_score = fuzz.ratio(
            str(batch_number).upper(),
            str(row["Batch_No"]).upper()
        )

        # Weighted score
        final_score = (
            0.50 * drug_score +
            0.30 * company_score +
            0.20 * batch_score
        )

        if final_score > best_score:

            best_score = final_score
            best_row = row

            best_drug_score = drug_score
            best_company_score = company_score
            best_batch_score = batch_score

    # No candidate passed the minimum drug-name similarity
    if best_row is None:
        return None

    # Overall confidence too low
    if best_score < MATCH_THRESHOLD:
        return None

    return {

        "matched_name": best_row["Drug_Name"],

        "drug_score": round(best_drug_score, 2),

        "manufacturer_score": round(best_company_score, 2),

        "batch_score": round(best_batch_score, 2),

        "overall_score": round(best_score, 2),

        "manufacturer": best_row["Manufacturer"],

        "batch_number": best_row["Batch_No"],

        "manufacturing_date": best_row["Manufacturing_Date"],

        "expiry_date": best_row["Expiry_Date"],

        "status": best_row["Status"],

        "risk_level": best_row["Risk_Level"],

        "failure_reason": best_row["Failure_Reason"],

        "laboratory": best_row["Laboratory"],

        "remarks": (
            None
            if pd.isna(best_row["Remarks"])
            else best_row["Remarks"]
        ),

        "source": best_row["Source"],

        "document": best_row["Document"]
    }


# Local test
if __name__ == "__main__":

    sample = {
        "drug_name": "Metronidazole Tablets",
        "manufacturer": "J.B. Chemicals & Pharmaceuticals Ltd",
        "batch_number": "BM325171"
    }

    print(find_match(sample))