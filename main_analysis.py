# main_analysis.py
import pandas as pd

def load_and_clean_data():
    df = pd.read_csv("netflix_titles.csv")

    # Clean data
    df = df.dropna(subset=['title'])
    df.fillna("Not Available", inplace=True)
    return df
