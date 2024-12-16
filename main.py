import sys
from task_manager import add_task, list_tasks, update_task, delete_task, update_task_status

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
    
    elif command == "update":
        if len(args) < 2:
            print("Error: Missing arguments for 'update'. Usage: update <id> <new description>")
        else:
            update_task(args[0], args[1])

    elif command == "delete":
        delete_task(args[0])

    elif command == "status":
        if len(args) < 2:
            print("Error: Missing arguments for 'status'. Usage: status <id> < new status>")
        else:
            update_task_status(args[0], args[1])

    else:
        print(f"Error: Unknown command '{command}'.")

if __name__ == "__main__":
    main()
