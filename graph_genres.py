from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import pandas as pd
import os

os.makedirs("plots", exist_ok=True)

df = load_and_clean_data()

genre_list = df['listed_in'].str.split(', ')
all_genres = [genre for sublist in genre_list for genre in sublist]
genre_count = Counter(all_genres)
genre_df = pd.DataFrame(genre_count.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

sns.barplot(x='Count', y='Genre', data=genre_df.head(10), palette='viridis')
plt.title('Top 10 Genres on Netflix')
plt.tight_layout()
# Save before showing; then show and close the figure
plt.savefig("plots/graph_genres.png", bbox_inches='tight')
plt.show()
plt.close()
print("✅ Graph saved as 'plots/graph_genres.png'")