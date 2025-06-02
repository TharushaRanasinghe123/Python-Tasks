# import requests
# from bs4 import BeautifulSoup
# import json

# all_data = []

# for page in range(1, 4):
#     url = f"https://quotes.toscrape.com/page/{page}/"
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "html.parser")
#     quotes = soup.find_all("div", class_="quote")
#     for q in quotes:
#         text = q.find("span", class_="text").text
#         author = q.find("small", class_="author").text
#         all_data.append({"quote": text, "author": author})

# with open("quotes.json", "w") as file:
#     json.dump(all_data, file, indent=2)

import requests
from bs4 import BeautifulSoup
import json

all_books = []

# Iterate through the first 3 pages
for page in range(1, 4):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # Find all book articles
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating_class = book.find("p", class_="star-rating")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

# Save to JSON file
with open("books.json", "w", encoding="utf-8") as file:
    json.dump(all_books, file, indent=2, ensure_ascii=False)


print("Done! Data saved to books.json")
