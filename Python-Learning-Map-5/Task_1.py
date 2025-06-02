import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# Extract title
title = soup.title.string
print("Page Title:", title)

# Extract all headers (h1 tags)
headers = soup.find_all('h1')
for h in headers:
    print("Header:", h.text)