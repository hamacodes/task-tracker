import unittest
import os
import json
from main import load_tasks, save_tasks

TEST_FILE = "test_tasks.json"


def load_test_tasks():
    """Load tasks from the test JSON file."""
    if not os.path.exists(TEST_FILE):
        with open(TEST_FILE, "w") as file:
            json.dump([], file)
    with open(TEST_FILE, "r") as file:
        return json.load(file)

def save_test_tasks(tasks):
    """Save tasks to the test JSON file."""
    with open(TEST_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

class TestTaskManagement(unittest.TestCase):
    def setUp(self):
        """Set up a fresh test file before each test."""
        with open(TEST_FILE, "w") as file:
            json.dump([], file)

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_load_empty_tasks(self):
        """Test loading tasks when the file is empty."""
        tasks = load_test_tasks()
        self.assertEqual(tasks, [], "The task list should be empty initially.")

    def test_save_and_load_tasks(self):
        """Test saving tasks and reloading them."""
        test_data = [
            {
                "id": 1,
                "description": "Test Task 1",
                "status": "todo",
                "createdAt": "2024-06-10 12:00:00",
                "updatedAt": "2024-06-10 12:00:00"
            }
        ]
        save_test_tasks(test_data)
        loaded_tasks = load_test_tasks()
        self.assertEqual(loaded_tasks, test_data, "The loaded tasks should match the saved tasks.")

    def test_append_task(self):
        """Test appending a task and saving it."""
        tasks = load_test_tasks()
        new_task = {
            "id": 2,
            "description": "Test Task 2",
            "status": "in-progress",
            "createdAt": "2024-06-10 12:05:00",
            "updatedAt": "2024-06-10 12:05:00"
        }
        tasks.append(new_task)
        save_test_tasks(tasks)
        
        # Verify the task was saved
        loaded_tasks = load_test_tasks()
        self.assertIn(new_task, loaded_tasks, "The new task should be in the task list.")

if __name__ == "__main__":
    unittest.main()