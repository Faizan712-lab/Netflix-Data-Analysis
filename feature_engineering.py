from main_analysis import load_and_clean_data
import pandas as pd

df = load_and_clean_data()

# Binary flags
df["is_movie"] = (df["type"].str.lower() == "movie").astype(int)
df["is_show"]  = (df["type"].str.lower() == "tv show").astype(int)

# Content breadth features
df["genre_count"] = df["listed_in"].astype(str).str.split(",").apply(lambda x: len([g for g in x if g.strip()]))

# Country diversity
countries = df["country"].astype(str).str.split(",").apply(lambda x: len([c for c in x if c.strip()]))
df["country_count"] = countries

# Release decade
df["release_decade"] = (df["release_year"] // 10 * 10).astype("Int64")

df.to_csv("cleaned_features.csv", index=False)
print("Saved engineered dataset: cleaned_features.csv")
