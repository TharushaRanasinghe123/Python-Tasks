import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}/"
all_quotes = []

for page in range(1, 4):
    res = requests.get(base_url.format(page))
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        all_quotes.append({"text": text, "author": author})

# Save to CSV
with open("quotes.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["text", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print("Quotes saved to quotes.csv")
