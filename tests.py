import os
import json
from main import load_tasks, save_tasks

TEST_FILE = "test_tasks.json"

# Override the load_tasks and save_tasks to use the test file
def load_test_tasks():
    """Load tasks from the test JSON file."""
    if not os.path.exists(TEST_FILE):
        with open(TEST_FILE, "w") as file:
            json.dump([], file)  # Create an empty test file
    with open(TEST_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_test_tasks(tasks):
    """Save tasks to the test JSON file."""
    with open(TEST_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Test function
def test():
    print("Testing JSON File Management...")
    tasks = load_test_tasks()
    print("Loaded tasks:", tasks)

    # Add a test task
    tasks.append({
        "id": 1,
        "description": "Test task",
        "status": "todo",
        "createdAt": "2024-06-10 12:00:00",
        "updatedAt": "2024-06-10 12:00:00"
    })

    save_test_tasks(tasks)
    print("Task saved successfully!")

    # Reload and check
    updated_tasks = load_test_tasks()
    print("Updated tasks:", updated_tasks)

    # Clean up the test file after running
    os.remove(TEST_FILE)
    print("Test file cleaned up.")

if __name__ == "__main__":
    test()