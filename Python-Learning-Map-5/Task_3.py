import requests
from bs4 import BeautifulSoup
import sqlite3
import time

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS quotes (text TEXT, author TEXT)")

for page in range(1, 4):
    try:
        url = f"https://quotes.toscrape.com/page/{page}/"
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            cursor.execute("INSERT INTO quotes (text, author) VALUES (?, ?)", (text, author))
        time.sleep(1)  # Rate limiting
    except Exception as e:
        print("Error occurred:", e)

conn.commit()
conn.close()
