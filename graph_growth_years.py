from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = load_and_clean_data()

df['release_year'].value_counts().sort_index().plot(kind='line', color='red')
plt.title('Netflix Content Growth Over the Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.tight_layout()
# Save before showing to avoid blank images
plt.savefig("plots/growth_years.png", bbox_inches='tight')
plt.show()
plt.close()
print("✅ Graph saved as 'plots/growth_years.png'")
