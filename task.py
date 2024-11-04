import os

# File to save tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "status": status == "complete"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "complete" if task["status"] else "incomplete"
            file.write(f"{task['task']} | {status}\n")

def display_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["status"] else "✗"
            print(f"{index}. {task['task']} [{status}]")

def add_task(tasks):
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "status": False})
    print("Task added successfully.")

def edit_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_index < len(tasks):
        new_task_name = input("Enter the new task name: ")
        tasks[task_index]["task"] = new_task_name
        print("Task edited successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["status"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def task_manager():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_complete(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

# Run the task manager
task_manager()
task.py
