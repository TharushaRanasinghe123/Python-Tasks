import pyodbc

# Replace with your server, database, and credentials
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-AT8UKAM\\SQLEXPRESS;'
    'DATABASE=SchoolDB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
print("Connection successful.")

name = 'Kamal Perera'
email = 'kamal@gmail.com'

cursor.execute("INSERT INTO Users (Name, Email) VALUES (?, ?)", (name, email))
conn.commit()
print("Data inserted successfully.")

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row.Id}, Name: {row.Name}, Email: {row.Email}")

conn.close()