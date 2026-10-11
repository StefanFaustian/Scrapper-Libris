import requests
from bs4 import BeautifulSoup

url = "https://www.libris.ro/carti/beletristica"

# For bypassing basic bot protection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Status: 200 - Connection successful!")
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("div", class_="pr-history-item")
    print(f"Found {len(books)} books on this page.")

    for book in books[:8]:
        title_element = book.find("div", class_="item-title")
        title = title_element.text.strip() if title_element else "No title found"

        price_element = book.find("p", class_="price-reduced")
        price = price_element.text.strip() if price_element else "No price found"

        print(f"Title: {title}")
        print(f"Price: {price}")
        print("-" * 40)
else:
    print(f"Connection failed. Status code: {response.status_code}")

