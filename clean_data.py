import pandas as pd

# Loading data into Pandas DataFrame 
df = pd.read_csv("books_data.csv")

df['Price'] = df['Price'].str.replace(' Lei', '', regex=False).str.strip()
# errors='coerce' will turn unconvertible elemnts to NaN
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
# Rows with invalid prices (e.g. NaN) are dropped
df = df.dropna(subset=['Price']) 

df.to_csv("books_clean.csv", index=False)