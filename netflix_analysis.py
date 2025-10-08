# Netflix Data Analysis - by Faizan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

print("✅ Dataset loaded successfully!")
print("Shape of the dataset:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

# Data Cleaning
# Drop rows where 'title' is missing (important column)
df = df.dropna(subset=['title'])

# Fill other missing values with "Not Available"
df.fillna("Not Available", inplace=True)

print("✅ Data cleaned successfully!")
print("Any missing values left?\n", df.isnull().sum().sum())

