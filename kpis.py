# file: kpis.py
import pandas as pd

df = pd.read_csv("cleaned_features.csv")

kpis = {
    "titles_total": len(df),
    "movies_share_pct": round(100 * (df["is_movie"].mean()), 2),
    "shows_share_pct": round(100 * (df["is_show"].mean()), 2),
    "median_genres_per_title": int(df["genre_count"].median()),
    "median_countries_per_title": int(df["country_count"].median()),
    "most_common_decade": int(df["release_decade"].mode(dropna=True).iat[0]),
}
pd.Series(kpis, dtype="object").to_json("plots/kpis.json", indent=2)
print("Saved KPIs to plots/kpis.json")
