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