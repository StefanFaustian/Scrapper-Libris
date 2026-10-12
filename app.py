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

    stl.sidebar.header("Filter Data")
    search_query = stl.sidebar.text_input("Search book title:", "")
    min_price = float(df['Price'].min())
    max_price = float(df['Price'].max())

    selected_max_price = stl.sidebar.slider(
        "Maximum Price (RON)",
        min_value=min_price,
        max_value=max_price,
        value=max_price
    )

    # A copy of the original dataframe is needed for filtering
    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df['Price'] <= selected_max_price]
    if search_query:
        filtered_df = filtered_df[filtered_df['Title'].str.contains(search_query, case=False)]

    stl.subheader("Market Overview")
    col1, col2, col3 = stl.columns(3)
    col1.metric("Total Books Analyzed", len(df))
    col2.metric("Average Price", f"{df['Price'].mean():.2f} RON")
    col3.metric("Cheapest Price", f"{df['Price'].min():.2f} RON")
    stl.divider()

    left_col, right_col = stl.columns([2, 1])
    with left_col:
        stl.subheader("Price Distribution")
        # Line chart resets index so the graph looks continuous even after filtering
        stl.line_chart(filtered_df["Price"].reset_index(drop=True))

    with right_col:
        stl.subheader("Raw Data View")
        stl.dataframe(df, use_container_width=True)

except:
    stl.error("Data file not found!")


