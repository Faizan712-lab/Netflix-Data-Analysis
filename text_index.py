# file: text_index.py
from main_analysis import load_and_clean_data
import pandas as pd
import re
import os

df = load_and_clean_data()

def normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

index = df[["show_id", "title", "description"]].copy()
index["title_norm"] = index["title"].astype(str).apply(normalize)
index["desc_norm"]  = index["description"].astype(str).apply(normalize)
os.makedirs("plots", exist_ok=True)

try:
    # Try to write parquet (requires pyarrow or fastparquet)
    index.to_parquet("plots/text_index.parquet", index=False)
    print("Saved normalized text index for search: plots/text_index.parquet")
except ImportError as e:
    # Fallback: write CSV and inform the user how to enable parquet support
    fallback = "plots/text_index.csv"
    index.to_csv(fallback, index=False)
    print("pyarrow/fastparquet not installed — saved CSV fallback:", fallback)
    print("To enable parquet output, install pyarrow (recommended) with:")
    print("  pip install pyarrow")
