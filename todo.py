FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = []
            for line in f:
                name, due, status = line.strip().split("|")
                tasks.append([name, due, status])
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write("|".join(task) + "\n")

def add_task(tasks):
    name = input("Task name: ").strip()
    due = input("Due date (YYYY-MM-DD): ").strip()
    tasks.append([name, due, "Pending"])
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    print("\nTasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t[0]} | Due: {t[1]} | {t[2]}")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        n = int(input("Task number to mark completed: "))
        tasks[n-1][2] = "Completed"
        save_tasks(tasks)
        print("Task marked as completed!")
    except:
        print("Invalid choice.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        n = int(input("Task number to delete: "))
        removed = tasks.pop(n-1)
        save_tasks(tasks)
        print("Deleted:", removed[0])
    except:
        print("Invalid choice.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1.Add  2.View  3.Complete  4.Delete  5.Exit")
        ch = input("Choice: ")

        if ch == "1":
            add_task(tasks)
        elif ch == "2":
            view_tasks(tasks)
        elif ch == "3":
            mark_completed(tasks)
        elif ch == "4":
            delete_task(tasks)
        elif ch == "5":
            break
        else:
            print("Invalid option.")

main()
