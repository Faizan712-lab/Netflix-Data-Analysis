# file: graph_duration.py
from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re, os

os.makedirs("plots", exist_ok=True)
df = load_and_clean_data()

movies = df[df["type"].str.lower() == "movie"].copy()
shows  = df[df["type"].str.lower() == "tv show"].copy()

def minutes_from_duration(x: str) -> float:
    if not isinstance(x, str): return float("nan")
    m = re.search(r"(\d+)\s*min", x.lower())
    return float(m.group(1)) if m else float("nan")

def seasons_from_duration(x: str) -> float:
    if not isinstance(x, str): return float("nan")
    m = re.search(r"(\d+)\s*season", x.lower())
    return float(m.group(1)) if m else float("nan")

movies["minutes"] = movies["duration"].map(minutes_from_duration)
shows["seasons"]  = shows["duration"].map(seasons_from_duration)

plt.figure(figsize=(7, 4))
sns.histplot(movies["minutes"].dropna(), bins=30, kde=True)
plt.title("Movie Duration (minutes)")
plt.tight_layout()
# Save before showing to ensure the PNG contains the rendered figure
plt.savefig("plots/movie_duration_hist.png", bbox_inches="tight")
plt.show()
plt.close()

plt.figure(figsize=(7, 4))
sns.countplot(x=shows["seasons"].dropna())
plt.title("TV Shows by Season Count")
plt.tight_layout()
plt.savefig("plots/tv_season_counts.png", bbox_inches="tight")
plt.show()
plt.close()

print("Saved: plots/movie_duration_hist.png, plots/tv_season_counts.png")
