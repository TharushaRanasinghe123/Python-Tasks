# main.py
import requests
from bs4 import BeautifulSoup
import json

all_data = []

for page in range(1, 4):
    url = f"https://quotes.toscrape.com/page/{page}/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        all_data.append({"quote": text, "author": author})

with open("quotes.json", "w") as file:
    json.dump(all_data, file, indent=2)
