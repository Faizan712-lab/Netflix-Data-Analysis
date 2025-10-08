# file: tests/test_data_quality.py
import pandas as pd

def test_no_empty_titles():
    df = pd.read_csv("cleaned_features.csv")
    assert (df["title"].astype(str).str.strip() != "").all()

def test_release_year_bounds():
    df = pd.read_csv("cleaned_features.csv")
    assert df["release_year"].between(1900, 2100).all()
