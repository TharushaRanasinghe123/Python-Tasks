import requests
from bs4 import BeautifulSoup


# Looping through multiple pages
for i in range(1, 4):
    url = f"https://example.com/page/{i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(f"Scraped page {i}")
