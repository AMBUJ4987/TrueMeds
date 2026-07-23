import os
import pdfplumber
import pandas as pd

# -----------------------------
# Folder Paths
# -----------------------------
PDF_FOLDER = "PDFS"
CSV_FOLDER = "CSV"
OUTPUT_FILE = os.path.join(CSV_FOLDER, "master.csv")

os.makedirs(CSV_FOLDER, exist_ok=True)

master_data = []

# -----------------------------
# Loop through PDFs
# -----------------------------
for pdf_file in os.listdir(PDF_FOLDER):

    if not pdf_file.lower().endswith(".pdf"):
        continue

    pdf_path = os.path.join(PDF_FOLDER, pdf_file)

    print(f"Processing: {pdf_file}")

    rows = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            table = page.extract_table()

            if table:
                rows.extend(table)

    if len(rows) < 2:
        print(f"Skipped: {pdf_file}")
        continue

    # ---------------------------------
    # Create dataframe
    # ---------------------------------

    header = []

    for i, col in enumerate(rows[0]):
        if col is None or str(col).strip() == "":
            header.append(f"Unnamed_{i}")
        else:
            col = str(col)
            col = col.replace("\n", " ")
            col = " ".join(col.split())
            header.append(col)

    data = rows[1:]

    df = pd.DataFrame(data, columns=header)

    # Remove duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # ---------------------------------
    # Clean every cell
    # ---------------------------------

    df = df.apply(
        lambda col: col.map(
            lambda x: " ".join(x.replace("\n", " ").split())
            if isinstance(x, str)
            else x
        )
    )

    # ---------------------------------
    # Detect Status
    # ---------------------------------

    filename = pdf_file.lower()

    if "spurious" in filename:
        status = "Spurious"
    elif "state" in filename:
        status = "NSQ"
    elif "nsq" in filename:
        status = "NSQ"
    elif "revise" in filename:
        status = "Revised Alert"
    else:
        status = "Unknown"

    # ---------------------------------
    # Detect Source
    # ---------------------------------

    if "state" in filename:
        source = "State Laboratory"
    elif "cdsco" in filename:
        source = "CDSCO"
    else:
        source = "CDSCO"

    df["Status"] = status
    df["Source"] = source
    df["Document"] = pdf_file

    # ---------------------------------
    # Debug
    # ---------------------------------

    print(df.columns.tolist())

    if df.columns.duplicated().any():
        print("DUPLICATE COLUMNS FOUND!")
        print(pdf_file)

    master_data.append(df)

# ---------------------------------
# Merge Everything
# ---------------------------------

master_df = pd.concat(master_data, ignore_index=True)

# ---------------------------------
# Remove Duplicate Rows
# ---------------------------------

master_df.drop_duplicates(inplace=True)

# ---------------------------------
# Save
# ---------------------------------

master_df.to_csv(OUTPUT_FILE, index=False)

print("\nDone!")
print(f"Rows : {len(master_df)}")
print(f"Saved : {OUTPUT_FILE}")