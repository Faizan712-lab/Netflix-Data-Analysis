from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

os.makedirs("plots", exist_ok=True)
df = load_and_clean_data()

def explode_list_column(frame: pd.DataFrame, col: str) -> pd.Series:
    s = frame[col].fillna("Not Available").astype(str).str.split(",")
    s = s.explode().str.strip()
    s = s[s.ne("Not Available") & s.ne("")]
    return s

top_dirs = explode_list_column(df, "director").value_counts().head(10)
top_cast = explode_list_column(df, "cast").value_counts().head(10)

fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(x=top_dirs.values, y=top_dirs.index, palette="mako", ax=ax)
ax.set_title("Top 10 Directors by Title Count")
fig.tight_layout()
# Save before showing, then display and close
fig.savefig("plots/top_directors.png", bbox_inches="tight")
plt.show()
plt.close(fig)

fig2, ax2 = plt.subplots(figsize=(7, 4))
sns.barplot(x=top_cast.values, y=top_cast.index, palette="crest", ax=ax2)
ax2.set_title("Top 10 Actors by Title Count")
fig2.tight_layout()
fig2.savefig("plots/top_actors.png", bbox_inches="tight")
plt.show()
plt.close(fig2)

print("Saved: plots/top_directors.png, plots/top_actors.png")
