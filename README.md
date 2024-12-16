---

# Task Tracker CLI

Task Tracker CLI is a simple command-line interface (CLI) tool to help you manage your tasks efficiently. You can add, update, delete, and list tasks, as well as mark tasks as "in-progress" or "done". Tasks are stored in a JSON file locally.

This project is a great way to practice file handling, user input parsing, and modular programming.

---

## Features

- Add a new task  
- Update task descriptions  
- Delete tasks  
- List all tasks or filter by status (`todo`, `in-progress`, `done`)  
- Mark tasks as "in-progress" or "done"  
- Tasks are stored persistently in a JSON file  

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repo-link>
   cd <project-folder>
   ```

2. Ensure you have Python 3 installed:
   ```bash
   python --version
   ```

3. No external dependencies are needed.

---

## Usage

### Available Commands

| Command                                | Description                                  |
|----------------------------------------|----------------------------------------------|
| `add "<description>"`                  | Add a new task                               |
| `list [status]`                        | List all tasks or filter by status           |
| `update <id> "<new description>"`      | Update the description of a task             |
| `delete <id>`                          | Delete a task by ID                          |
| `status <id> <new_status>`             | Update the status of a task (`todo`, `in-progress`, `done`) |
| `help`                                 | Display help information                     |

---

### Examples

1. **Add a Task**
   ```bash
   python main.py add "Complete the Python project"
   ```
   Output:
   ```
   Task added successfully (ID: 1).
   ```

2. **List All Tasks**
   ```bash
   python main.py list
   ```

3. **List Tasks by Status**
   ```bash
   python main.py list in-progress
   ```

4. **Update a Task**
   ```bash
   python main.py update 1 "Write project documentation"
   ```

5. **Delete a Task**
   ```bash
   python main.py delete 1
   ```

6. **Update Task Status**
   ```bash
   python main.py status 2 done
   ```

7. **View Help**
   ```bash
   python main.py help
   ```

---

## File Structure

```
task-tracker/
├── main.py            # Entry point for the CLI
├── task_manager.py    # Core task management functions
├── tasks.json         # Task data (auto-generated)
└── tests.py           # Unit tests for the project
```

---

## Learning Resource

This project is inspired by the [Task Tracker Roadmap](https://roadmap.sh/projects/task-tracker).  
