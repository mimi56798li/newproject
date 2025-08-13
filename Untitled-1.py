"""
Simple To-Do List App
---------------------
Features:
1. Add tasks
2. View all tasks
3. Remove a task
4. Save tasks to file (so they're not lost after closing)

This is beginner-friendly and uses only Python basics.
"""

# -------------------------------
# Step 1: Define the file to store tasks
# -------------------------------
TASKS_FILE = "tasks.txt"  # The file where tasks will be saved

# -------------------------------
# Step 2: Load existing tasks from file
# -------------------------------
def load_tasks():
    """
    Reads tasks from the file and returns them as a list.
    If the file does not exist yet, it returns an empty list.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.read().splitlines()  # split by new lines
        return tasks
    except FileNotFoundError:
        return []  # no tasks yet


# -------------------------------
# Step 3: Save tasks to file
# -------------------------------
def save_tasks(tasks):
    """
    Writes the list of tasks to the file.
    Each task is stored on a new line.
    """
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# -------------------------------
# Step 4: Display all tasks
# -------------------------------
def view_tasks(tasks):
    """Prints all the tasks to the console in a numbered list."""
    if not tasks:
        print("\nNo tasks yet. Add some!\n")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()  # extra newline


# -------------------------------
# Step 5: Add a new task
# -------------------------------
def add_task(tasks):
    """Asks the user for a task and adds it to the list."""
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"Task '{new_task}' added successfully!\n")
    else:
        print("Empty task not added.\n")


# -------------------------------
# Step 6: Remove a task
# -------------------------------
def remove_task(tasks):
    """Removes a task based on its number in the list."""
    if not tasks:
        print("No tasks to remove.\n")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# -------------------------------
# Step 7: Main Program Loop
# -------------------------------
def main():
    tasks = load_tasks()  # load saved tasks at start

    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)  # save before exiting
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please choose 1-4.\n")


# -------------------------------
# Step 8: Run the program
#
