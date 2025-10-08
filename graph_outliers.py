from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("plots", exist_ok=True)
df = load_and_clean_data()

num_cols = df.select_dtypes(include="number").columns.tolist()
for col in num_cols:
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.boxplot(x=df[col], ax=ax)
    ax.set_title(f"Outliers: {col}")
    fig.tight_layout()
    # Save
    out_path = f"plots/outliers_{col}.png"
    fig.savefig(out_path, bbox_inches="tight")
    plt.show()
    plt.close(fig)
    print(f"Saved: {out_path}")
print("Saved: plots/outliers_*.png")
