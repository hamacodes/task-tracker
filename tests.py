import unittest
import os
import json
from task_manager import load_tasks, save_tasks, add_task

TEST_FILE = "test_tasks.json"

def load_test_tasks():
    if not os.path.exists(TEST_FILE):
        with open(TEST_FILE, "w") as file:
            json.dump([], file)
    with open(TEST_FILE, "r") as file:
        return json.load(file)

def save_test_tasks(tasks):
    with open(TEST_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Set up a fresh test file."""
        with open(TEST_FILE, "w") as file:
            json.dump([], file)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        """Test adding a task."""
        add_task("Test Task")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Test Task")

if __name__ == "__main__":
    unittest.main()
