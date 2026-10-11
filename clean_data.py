import pandas as pd

# Loading data into Pandas DataFrame 
df = pd.read_csv("books_data.csv")

print(df.head())

df['Price'] = df['Price'].str.replace(' Lei', '', regex=False).str.strip()
# errors='coerce' will turn unconvertible elemnts to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
# Rows with invalid prices (e.g. NaN) are dropped
df = df.dropna(subset=['Price']) 

print("\n------CLEANED DATA ------")
print(df.head())

print("\n---QUICK STATS ---")
print(f"Average price: {df['Price'].mean():.2f} Lei")
print(f"Most expensive: {df['Price'].max()} Lei")
print(f"Cheapest: {df['Price'].min()} Lei")

df.to_csv("books_clean.csv", index=False)