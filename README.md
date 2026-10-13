# 📖 Libris Book Prices ETL Pipeline & Dashboard

## Project Overview
This is a complete end-to-end pipeline (ETL) designed to extract, clean, and visualize book prices from the Romanian bookstore, Libris.ro. The project demonstrates the ability to collect raw web data, process it into an analytical format, and deploy an interactive dashboard for real-time market analysis.

## Features
* **Extract (Web Scraping):** Automated, polite scraping of multiple pages using `BeautifulSoup` and `requests`. Handles dynamic pagination parameters.
* **Transform (Data Cleaning):** Uses `pandas` to process raw text, remove currency strings, handle missing values, and convert data types for statistical analysis.
* **Load (Data Visualization):** An interactive web application built with `Streamlit` and `Plotly`, featuring:
  * Dynamic filtering (Text Search & Price Slider).
  * Hover-enabled data tooltips for individual book insights.
  * Real-time recalculation of market KPIs (Average Price, Cheapest Book).

## Tools & Technologies
* **Language:** Python 3.12 (newer versions are not supported by `pandas`)
* **Data Extraction:** `requests`, `BeautifulSoup4`
* **Data Wrangling:** `pandas`
* **Dashboard & Visualization:** `streamlit`, `plotly`

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/StefanFaustian/Scrapper-Libris.git
   cd Scrapper-Libris
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv .venv
   # On Windows:
   .\.venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Step-by-step Guide
To run the full pipeline, execute the scripts sequentially:

**Step 1: Extract Data**
Run the web scraper to collect data from the website.
```bash
python main.py
```

**Step 2: Clean Data**
Process the raw `.csv` file into a clean, analytical format.
```bash
python clean_data.py
```

**Step 3: Launch the Dashboard**
Start the Streamlit server to interact with the data visually.
```bash
streamlit run app.py
```