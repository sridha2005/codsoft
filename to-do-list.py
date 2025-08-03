import json
def load_task():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
            return []
def save_tasks(tasks):
    with open("tasks.json", "w")  as file:
        json.dump(tasks,file)
def add_task(tasks):
    task = input("Enter the task:")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!")
def show_tasks(tasks):
    for idx, task in enumerate(tasks, 1):
        status = " correct" if task["done"] else "wrong"
        print(f"{idx}. {task['task']} [{status}]")
def mark_done(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to mark as done:"))-1
    if 0 <= num< len(tasks):
        tasks[num]["done"] = true
        print("Task marked as done.")
def delete_task(tasks):
    show_tasks(tasks)
    num = int(input("Enter task number to delete:"))-1
    if 0 <= num < len(tasks):
        tasks.pop(num)
        print("Task deleted.")
def main():
    tasks = load_task()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("choose an option:")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
