todos = []

def show_todos():
    if len(todos) == 0:
        print("\n📭 No tasks found!")
    else:
        print("\n📋 Your Todo List:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")

def add_todo():
    task = input("Enter task: ")
    todos.append(task)
    print(f"✅ '{task}' added successfully!")

def delete_todo():
    show_todos()
    num = int(input("Enter task number to delete: "))
    removed = todos.pop(num - 1)
    print(f"🗑️ '{removed}' deleted successfully!")

while True:
    print("\n--- Todo App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        delete_todo()
    elif choice == "4":
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice!")
        