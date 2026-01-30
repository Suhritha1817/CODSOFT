# Simple & Human-Friendly To-Do List App

def show_menu():
    print("\n📌 TO-DO LIST MENU")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")


tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✔ Done" if t["done"] else "⏳ Pending"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("📭 No tasks to mark.")
        else:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("🎉 Task marked as completed!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("📭 No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑 Task '{removed['task']}' deleted.")
            else:
                print("❌ Invalid task number.")

    elif choice == "5":
        print("👋 Thank you for using the To-Do List. Stay productive!")
        break

    else:
        print("⚠ Please choose a valid option (1–5).")
