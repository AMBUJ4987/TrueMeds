import pandas as pd

from rapidfuzz import process, fuzz


# Load the dataset once
master_df = pd.read_csv(
    r"E:\TrueMeds\DATASET\CSV\master_final.csv"
)

medicine_names = (
    master_df["Drug_Name"]
    .fillna("")
    .astype(str)
    .tolist()
)

import re

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

    # Remove numbers like 400, 500, etc.
    name = re.sub(r"\d+", "", name)

    # Remove punctuation
    name = re.sub(r"[^a-z ]", "", name)

    return " ".join(name.split())

def find_match(drug_name):

    if not drug_name:
        return None

    normalized_query = normalize_name(drug_name)

    normalized_database = [
        normalize_name(x)
        for x in medicine_names
]

    match = process.extractOne(
        normalized_query,
        normalized_database,
        scorer=fuzz.token_sort_ratio
)

    if match is None:
        return None

    matched_name = match[0]
    score = match[1]
    index = match[2]

    row = master_df.iloc[index]

    return {

        "matched_name": matched_name,

        "similarity_score": round(score, 2),

        "manufacturer": row["Manufacturer"],

        "batch_number": row["Batch_No"],

        "manufacturing_date": row["Manufacturing_Date"],

        "expiry_date": row["Expiry_Date"],

        "status": row["Status"],

        "risk_level": row["Risk_Level"],

        "failure_reason": row["Failure_Reason"],

        "laboratory": row["Laboratory"],

        "remarks": (
            None
            if pd.isna(row["Remarks"])
            else row["Remarks"]
),

        "source": row["Source"],

        "document": row["Document"]
    }


if __name__ == "__main__":

    result = find_match("Metronidazole IP")

    print(result)