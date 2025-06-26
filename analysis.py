# CareerFoundry Data Analysis Project
# Author: Manasa Ungarala

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Step 1: Load the dataset ===
df = pd.read_csv("data/customer_data.csv")  # replace with actual CSV
print("✅ Data loaded. Shape:", df.shape)

# === Step 2: Basic data cleaning ===
df.dropna(inplace=True)
df['Total_Purchase'] = df['Total_Purchase'].astype(float)
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

# === Step 3: Exploratory Data Analysis (EDA) ===
print("📊 Descriptive Statistics:\n", df.describe())

# Purchase distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Total_Purchase'], bins=30, kde=True)
plt.title("Customer Purchase Distribution")
plt.xlabel("Total Purchase Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("purchase_distribution.png")
plt.close()

# RFM Analysis (Recency, Frequency, Monetary)
df['Days_Since_Join'] = (pd.Timestamp.today() - df['Join_Date']).dt.days
rfm = df.groupby('Customer_ID').agg({
    'Days_Since_Join': 'min',
    'Total_Purchase': ['count', 'sum']
}).reset_index()

rfm.columns = ['Customer_ID', 'Recency', 'Frequency', 'Monetary']
print("📦 RFM Table:\n", rfm.head())

# === Step 4: Save Cleaned Data ===
df.to_csv("data/cleaned_customer_data.csv", index=False)
print("✅ Cleaned data saved.")
