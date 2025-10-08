# file: recommender.py
import os
import pandas as pd
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    raise ImportError(
        "scikit-learn is required to run recommender.py.\n"
        "Install it with: python -m pip install --upgrade pip; python -m pip install scikit-learn\n"
        "Or with conda: conda install -c conda-forge scikit-learn"
    )

# Robustly load the text index: prefer parquet, fall back to CSV with clear errors
index_parquet = "plots/text_index.parquet"
index_csv = "plots/text_index.csv"

if os.path.exists(index_parquet):
    try:
        idx = pd.read_parquet(index_parquet)
    except ImportError:
        # Parquet engine missing — try CSV fallback
        if os.path.exists(index_csv):
            print("Parquet engine not available — falling back to CSV index")
            idx = pd.read_csv(index_csv)
        else:
            raise
elif os.path.exists(index_csv):
    idx = pd.read_csv(index_csv)
else:
    raise FileNotFoundError(
        "No text index found. Run text_index.py first (it writes plots/text_index.parquet or CSV fallback)."
    )

# Ensure normalized text columns exist (created by text_index.py); if not, create simple defaults
if "title_norm" not in idx.columns:
    idx["title_norm"] = idx.get("title", "").astype(str).str.lower()
if "desc_norm" not in idx.columns:
    idx["desc_norm"] = idx.get("description", "").astype(str).str.lower()

corpus = (idx["title_norm"].fillna("") + " " + idx["desc_norm"].fillna("")).tolist()

# Vectorizer — tune min_df if your corpus is small
tfidf = TfidfVectorizer(min_df=3, max_df=0.9, ngram_range=(1,2))
X = tfidf.fit_transform(corpus)

def recommend(title_query: str, top_k: int = 5):
    q = title_query.lower()
    q_vec = tfidf.transform([q])
    sims = cosine_similarity(q_vec, X).ravel()
    top = sims.argsort()[::-1][:top_k]
    return idx.iloc[top][["show_id", "title"]]

def build_gui():
    root = tk.Tk()
    root.title("Simple Netflix Recommender")
    root.geometry("700x400")

    frm = ttk.Frame(root, padding=10)
    frm.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frm, text="Enter a search query (title or keywords):").pack(anchor=tk.W)
    qvar = tk.StringVar()
    entry = ttk.Entry(frm, textvariable=qvar)
    entry.pack(fill=tk.X, pady=6)

    result_frame = ttk.Frame(frm)
    result_frame.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

    cols = ("show_id", "title")
    tree = ttk.Treeview(result_frame, columns=cols, show="headings")
    tree.heading("show_id", text="ID")
    tree.heading("title", text="Title")
    tree.column("show_id", width=120, anchor=tk.W)
    tree.column("title", width=540, anchor=tk.W)
    tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    vsb = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=vsb.set)

    def on_recommend(event=None):
        q = qvar.get().strip()
        if not q:
            messagebox.showinfo("Input needed", "Please enter a search query.")
            return
        try:
            df = recommend(q, top_k=10)
        except Exception as e:
            messagebox.showerror("Error", f"Recommendation failed: {e}")
            return

        # Clear existing rows
        for r in tree.get_children():
            tree.delete(r)

        if df.empty:
            messagebox.showinfo("No results", "No recommendations found for this query.")
            return

        for _, row in df.iterrows():
            tree.insert("", tk.END, values=(row.get("show_id", ""), row.get("title", "")))

    btn = ttk.Button(frm, text="Recommend", command=on_recommend)
    btn.pack(pady=6)

    entry.bind("<Return>", on_recommend)
    entry.focus()

    root.mainloop()


if __name__ == "__main__":
    try:
        build_gui()
    except Exception as e:
        # If GUI fails, print helpful message
        print("Failed to start GUI:", e)
        print("You can still call recommend(title, top_k) from Python code.")
