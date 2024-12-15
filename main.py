import sys
import json
import os


TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file"""
    if not os.path.exists(TASKS_FILE):
        # File does not exist, create an empty file
        with open(TASKS_FILE, "w") as file:
            json.dump([], file) # Write empty list to the file

        
    # File does exist:
    with open(TASKS_FILE, "r") as file:
        try:
            tasks = json.load(file)
            return tasks
        except json.JSONDecodeError:
            return [] # File is invalid, return empty list

def save_tasks(tasks):
    """Savee tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)



def main():
    # Check if any arguements are passed
    if len(sys.argv) < 2:
        print("Error: No command provided. Use 'add', 'update', 'delete', 'list', etc.")
        return
    
    # Extract command (first argument)
    command = sys.argv[1]
    args = sys.argv[2:] # Remaining arguments

    # Handle different commands
    if command == "add":
        if len(args) < 1:
            print("Error: Missing task description for 'add'.")
        else:
            print(f"Command: add | Task Description: {args[0]}")
    elif command == "update":
        if len(args) < 2:
            print("Error: Missing arguments for 'update'. Usage: update <id> <new description>")
        else:
            print(f"Command: update | ID: {args[0]} | New Description: {args[1]}")
    elif command == "delete":
        if len(args) < 1:
            print("Error: Missing task ID for 'delete'.")
        else:
            print(f"Command: delete | ID: {args[0]}")
    elif command == "list":
        status_filter = args[0] if args else "all"
        print(f"Command: list | Status: {status_filter}")
    elif command in ["mark-in-progress", "mark-done"]:
        if len(args) < 1:
            print(f"Error: Missing task ID for '{command}'.")
        else:
            print(f"Command: {command} | ID: {args[0]}")
    else:
        print(f"Error: Unknown command '{command}'.")


if __name__ == "__main__":
    main()