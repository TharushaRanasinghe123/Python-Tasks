import json
from datetime import datetime

# Budget data
transactions = []

# Load previous data
def load_data():
    try:
        with open("budget_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data
def save_data():
    with open("budget_data.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Add a transaction
def add_transaction(type_, category, amount):
    transaction = {
        "type": type_,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    transactions.append(transaction)
    print(f"{type_} added: {amount} under {category}")

# Show summary
def show_summary():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Balance: {income - expenses}")

# Main loop
transactions = load_data()
while True:
    print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        cat = input("Enter income category: ")
        amt = float(input("Enter amount: "))
        add_transaction("income", cat, amt)
    elif choice == "2":
        cat = input("Enter expense category: ")
        amt = float(input("Enter amount: "))
        add_transaction("expense", cat, amt)
    elif choice == "3":
        show_summary()
    elif choice == "4":
        save_data()
        print("Data saved. Goodbye!")
        break
    else:
        print("Invalid choice.")
