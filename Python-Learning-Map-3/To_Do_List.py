import json
import os

filename = "tasks.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx+1}. [{status}] {task['title']} (Due: {task['due_date']})")

def add_task(tasks, title, due_date):
    tasks.append({"title": title, "completed": False, "due_date": due_date})

def mark_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

# CLI usage
tasks = load_tasks()
while True:
    print("\n1. View tasks\n2. Add task\n3. Complete task\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        title = input("Task title: ")
        due = input("Due date: ")
        add_task(tasks, title, due)
    elif choice == "3":
        idx = int(input("Task number to mark complete: ")) - 1
        mark_complete(tasks, idx)
    elif choice == "4":
        save_tasks(tasks)
        break
