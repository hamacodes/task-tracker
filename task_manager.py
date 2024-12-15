import json
import os
import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load taks from the JSON file."""

    # JSON doesn't exist:
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            json.dump([], file)
    
    # JSON does exist:
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task to the tasks list."""
    tasks = load_tasks()
    
    if tasks:
        new_id = tasks[-1]["id"] + 1    # new_id = last task's id + 1
    else:
        new_id = 1  # no tasks, so id starts a 1
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id}).")


def list_tasks(status=None):
    """
    List all tasks or filter them by status.

    Args:
        status (str): Optional status to filter tasks (todo, in-progress, done).
    """

    tasks = load_tasks()

    # Check if status argument was provided:
    if status:
        filtered_tasks = [task for task in tasks if task["status"] == status]
    else:
        filtered_tasks = tasks
    
    if not filtered_tasks:
        print("No tasks found." if not status else f"No tasks with status '{status}' found.")
        return
    
    # Display tasks using formated f strings
    print("\nTasks:")
    print(f"{'ID':<5} {'Description':<30} {'Status':<12} {'Created At'}")
    print("-" * 70)
    for task in filtered_tasks:
        print(f"{task['id']:<5} {task['description']:<30} {task['status']:<12} {task['createdAt']}")
    print()