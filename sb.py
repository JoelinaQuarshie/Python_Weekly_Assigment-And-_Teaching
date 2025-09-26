import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("coffe_sales.csv")  # Make sure coffe_sales.csv is in the same directory

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore the structure
print("Data types:")
print(df.dtypes)

print("Missing values in each column:")
print(df.isnull().sum())

# Step 4: Clean the dataset
# Option A: Drop rows with any missing values
df_cleaned = df.dropna()

# Show cleaned dataset info
print("Dataset after cleaning (first 5 rows):")
print(df_cleaned.head())

# Step 5: Compute basic statistics
print("Basic Statistics (describe):")
print(df_cleaned.describe())

# Step 6: Group by hour of day and compute mean
print("Mean of numerical features grouped by hour of day:")
grouped_means = df_cleaned.groupby("hour_of_day").mean(numeric_only=True)
print(grouped_means)

# Step 7: Identify patterns
print("Interesting findings:")

# Set seaborn theme for better aesthetics
sns.set(style="whitegrid")

# -------------------------------
# 1. Line Chart (simulated trend)
# -------------------------------
# We'll simulate a time-series by plotting money received per hour of the day
plt.figure(figsize=(10, 5))
sns.lineplot(data = df_cleaned, x="hour_of_day", y="money", marker='o',color='green',)
plt.title("Simulated Time Trend of money received")
plt.xlabel("hour of day")
plt.ylabel("money_received")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart: Average Sales per Product
# -------------------------------
plt.figure(figsize=(10, 5))
sns.barplot(data=df_cleaned, x="coffee_name", y="money", estimator="mean", hue="coffee_name", palette="viridis", legend=False)
plt.title("Average Money Received per Product")
plt.xlabel("name of coffee")
plt.ylabel("Average Sales (Money)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])  
daily_sales = df_cleaned.groupby('Date')['money'].sum()
daily_sales.plot(kind='line', figsize=(10,5), title='Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Money')
plt.grid(True)
plt.tight_layout()
plt.show()

# Extract month name from the date
df_cleaned['Month_name'] = pd.to_datetime(df_cleaned['Date']).dt.month_name()

# Set correct month order
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
df_cleaned['Month_name'] = pd.Categorical(df_cleaned['Month_name'], categories=month_order, ordered=True)

# Create pivot table: rows = hour, columns = month, values = average money
pivot = df_cleaned.pivot_table(
    index='hour_of_day',
    columns='Month_name',
    values='money',
    aggfunc='mean'
)

# Plot heatmap
sns.heatmap(pivot, cmap='YlGnBu', annot=True, fmt=".1f")
plt.title("Average Money Received by Hour and Month")
plt.tight_layout()
plt.show()
