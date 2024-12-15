import sys
from task_manager import add_task, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        if len(args) < 1:
            print("Error: Missing task description for 'add'.")
        else:
            add_task(args[0])
    elif command == "list":
        status = args[0] if args else None # Optional status arg
        list_tasks(status)
    else:
        print(f"Error: Unknown command '{command}'.")

if __name__ == "__main__":
    main()
