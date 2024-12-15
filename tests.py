from main import load_tasks, save_tasks



def test():
    print("Testing JSON File Management...")
    tasks = load_tasks()
    print("Loaded tasks:", tasks)
    
    # Adding a test task
    tasks.append({
        "id": 1,
        "description": "Test task",
        "status": "todo",
        "createdAt": "2024-06-10 12:00:00",
        "updatedAt": "2024-06-10 12:00:00"
    })
    
    save_tasks(tasks)
    print("Task saved successfully!")

if __name__ == "__tests__":
    test()