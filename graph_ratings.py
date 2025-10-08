# file: graph_ratings.py
from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

os.makedirs("plots", exist_ok=True)
df = load_and_clean_data()

rating_counts = df["rating"].fillna("Not Available").value_counts().sort_values(ascending=False)

plt.figure(figsize=(8, 4))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis")
plt.xticks(rotation=45, ha="right")
plt.title("Titles by Rating")
plt.tight_layout()
# Save before showing to ensure the saved file contains the plot
plt.savefig("plots/ratings_counts.png", bbox_inches="tight")
plt.show()
plt.close()

year_bins = pd.cut(df["release_year"], bins=10)
pivot = df.groupby([year_bins, df["rating"].fillna("Not Available")]).size().unstack(fill_value=0)

plt.figure(figsize=(10, 5))
sns.heatmap(pivot.T, cmap="rocket", cbar_kws={"label": "Number of titles"})
plt.title("Rating vs Release Year (binned)")
plt.tight_layout()
# Save heatmap before showing
plt.savefig("plots/ratings_year_heatmap.png", bbox_inches="tight")
plt.show()
plt.close()

print("Saved: plots/ratings_counts.png, plots/ratings_year_heatmap.png")
