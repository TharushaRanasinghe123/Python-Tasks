import csv

# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample text file.")

# Reading from a text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Text File Content:", content)


# Create a CSV file from a list of dictionaries
data = [
    {"name": "Nimasha", "age": 25},
    {"name": "Himasha", "age": 30}
]

with open("people.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)

# Read the CSV file back
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)