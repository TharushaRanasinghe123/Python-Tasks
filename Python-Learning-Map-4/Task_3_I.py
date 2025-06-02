from pymongo import MongoClient

# Connect to local MongoDB instance
client = MongoClient("mongodb://localhost:27017/")

# Create or connect to a database
db = client["companyDB"]

# Create or connect to a collection
employees_collection = db["employees"]

print("Connected to MongoDB successfully.")

employees = [
    {"name": "Kamal", "role": "Developer", "age": 25},
    {"name": "Amal", "role": "Manager", "age": 30},
    {"name": "Nimal", "role": "Designer", "age": 28}
]

# Insert into the collection
employees_collection.insert_many(employees)
print("Employees inserted successfully.")

print("Fetching documents:")
for employee in employees_collection.find():
    print(employee)

# --- UPDATE ---
# Update Amal's role from Manager to Senior Manager
update_result = employees_collection.update_one(
    {"name": "Amal"},
    {"$set": {"role": "Senior Manager"}}
)
print(f"\nUpdated {update_result.modified_count} document(s).")

# --- DELETE ---
# Delete the employee named Nimal
delete_result = employees_collection.delete_one({"name": "Nimal"})
print(f"\nDeleted {delete_result.deleted_count} document(s).")

# --- FILTER ---
# Find all employees with role = Developer
print("\nEmployees with role 'Developer':")
for employee in employees_collection.find({"role": "Developer"}):
    print(employee)