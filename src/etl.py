from datetime import datetime
import numpy as np
import pandas as pd
from src import config
import sys
import os

# Load all data sheets
try:
    xls = pd.ExcelFile(config.FILE_PATH)
    print("Sheets found:", xls.sheet_names)
except Exception as e:
    print(f"Error loading Excel file at {config.FILE_PATH}: {e}")
    sys.exit(1)

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Bad values
bad_values = ["[u]", "[z]"]

# Process each sheet 
for sheet in xls.sheet_names:

    # Skip Cover_Sheet and Notes (non-data sheets)
    if sheet in config.SKIP_SHEETS:
        print(f"Skipping sheet: {sheet}")
        continue

    try:
        df = pd.read_excel(xls, sheet_name=sheet)
    except Exception as e:
        print(f"Error reading sheet {sheet}: {e}")
        continue

    if df.empty:
        print(f"Sheet {sheet} is empty, skipping")
        continue
    
    # Drop empty columns
    df = df.loc[:, ~df.columns.str.contains(r"^unnamed", case=False, na=False)]
    df = df.dropna(axis=1, how="all") 

    # Normalise column names after loading
    df.columns = (
        df.columns
        .astype(str)
        .str.replace(r"\s+"," ",regex=True)
        .str.replace(r"\s*\[", " [", regex=True)
        .str.strip()
        .str.lower()
    )

    # Fuzzy rename columns based on expected patterns
    new_columns = {}

    for col in df.columns:
        col_clean = col.lower()
        if "recorded station stops" in col_clean and "(percentage)" in col_clean:
            new_columns[col] = "recorded_station_stops_%"
        elif "time to 3" in col_clean:
            new_columns[col] = "time_to_3_%"
        elif "cancellations" in col_clean:
            new_columns[col] = "cancellations_%"
    df = df.rename(columns=new_columns)

    # Numeric cleaning
    target_cols = [
        config.BUSINESS_RULE["stops_col"],
        config.BUSINESS_RULE["time_col"],
        config.BUSINESS_RULE["cancel_col"]
    ]
    for col in target_cols:
        if col in df.columns:
            df[col] = df[col].replace(bad_values, np.nan)

            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Add source sheet column for traceability (for Power BI)
    df["source_sheet"] = sheet

    # Clean sheet names
    clean_name = sheet.split(" ", 1)[1] if " " in sheet else sheet
    
    file_name = clean_name.replace(" ","_").lower() + ".csv"

    # Save cleaned data to CSV outputs with date
    output_path = f"output/{datetime.now().strftime('%Y-%m-%d')}_{file_name}"
    
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data for sheet {sheet} to {output_path}")

print("All sheets processed successfully!")
