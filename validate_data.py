# file: validate_data.py
from main_analysis import load_and_clean_data
import pandas as pd

df = load_and_clean_data()

report = {
    "row_count": len(df),
    "column_count": df.shape[1],
    "null_summary": df.replace("Not Available", pd.NA).isna().sum().to_dict(),
    "unique_types": df["type"].dropna().unique().tolist(),
    "year_range": (df["release_year"].min(), df["release_year"].max()),
    "duplicate_titles": int(df.duplicated(subset=["title", "release_year"]).sum()),
}
pd.Series(report, dtype="object").to_json("plots/data_quality_report.json", indent=2)
print("Wrote data_quality_report.json")
