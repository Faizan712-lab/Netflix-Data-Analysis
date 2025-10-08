from main_analysis import load_and_clean_data
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("plots", exist_ok=True)

df = load_and_clean_data()

# Create the bar chart
ax = df['country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Content-Producing Countries')
plt.xlabel('Country')
plt.ylabel('Number of Titles')

# Save 
plt.savefig("plots/top_countries.png", bbox_inches='tight')
plt.show()
plt.close()
print("✅ Graph saved as 'plots/top_countries.png'")