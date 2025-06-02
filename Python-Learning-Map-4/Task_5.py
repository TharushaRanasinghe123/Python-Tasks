import sqlite3
import json

# Setup DB
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER
)
''')

# Add products
products = [("Laptop", 10), ("Monitor", 5)]
cursor.executemany("INSERT INTO products (name, quantity) VALUES (?, ?)", products)
conn.commit()

# Export to JSON
cursor.execute("SELECT * FROM products")
products_data = cursor.fetchall()
product_list = [{"id": p[0], "name": p[1], "quantity": p[2]} for p in products_data]

with open("inventory.json", "w") as f:
    json.dump(product_list, f, indent=4)

# Display JSON content
with open("inventory.json", "r") as f:
    data = json.load(f)
    print("Inventory JSON:", data)

conn.close()
