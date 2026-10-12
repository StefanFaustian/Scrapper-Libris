import streamlit as stl
import pandas as pd

# Webpage's head tags
stl.set_page_config(page_title="Book Prices Overview", page_icon="📖", layout="wide")

# Webpage's main title
stl.title("Book Prices Overview - Libris")
stl.markdown("Welcome, dear reader! This tool analyzes book prices extracted directly from the web.")

@stl.cache_data # ensures the file is loaded only once
def load_data():
    return pd.read_csv("books_clean.csv")

try:
    df = load_data()
    stl.subheader("Market Overview")
    col1, col2, col3 = stl.columns(3)
    col1.metric("Total Books Analyzed", len(df))
    col2.metric("Average Price", f"{df['Price'].mean():.2f} RON")
    col3.metric("Cheapest Price", f"{df['Price'].min():.2f} RON")
    stl.divider()

    left_col, right_col = stl.columns([2, 1])
    with left_col:
        stl.subheader("Price Distribution")
        stl.line_chart(df["Price"])

    with right_col:
        stl.subheader("Raw Data View")
        stl.dataframe(df, use_container_width=True)

except:
    stl.error("Data file not found!")


