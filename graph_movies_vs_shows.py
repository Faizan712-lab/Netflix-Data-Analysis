from main_analysis import load_and_clean_data
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("plots", exist_ok=True)

df = load_and_clean_data()

sns.countplot(x='type', data=df, palette='coolwarm')
plt.title('Movies vs TV Shows on Netflix')

# Save before showing and close the figure to ensure the PNG contains the plot
plt.savefig("plots/movies_vs_tvshows.png", bbox_inches='tight')
plt.show()
plt.close()
print("✅ Graph saved as 'plots/movies_vs_tvshows.png'")
