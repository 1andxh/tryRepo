print("\nWelcome to The To-do List\n".ljust(50, "="))


# print menu
def menu():
    print('1. Add task')
    print('2. Remove task')
    print('3. Mark task as complete')
    print('4. View task task')


# add task
def add_task(tasks):
    task_name = input("Enter task to add: ")
    tasks[task_name] = False
    if len(task_name) > 1:
        task_name == []
    print(f"Task |{task_name}| has been added successfully")

# mark task as complete
def mark_complete(tasks):
        task_name = input('Enter task name to mark: ')
        if task_name in tasks:
            tasks[task_name] = True
            print(f"Task |{task_name}| has been marked complete")
        else:
            print(f"Task |{task_name}| cannot be found or is no")

# remove task
def remove_task(tasks):
    task_name = input('Enter task to remove: ')
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task |{tasks}| was successfully removed")
    else:
        print(f"could not find |{tasks}|")

# view task
def view_task(tasks):
    print("\nCurent Tasks:")
    for task, complete in tasks.items():
        if complete:
            status = "Complete"
        else:
            status = "Incomplete"
        print(f"{task}: {status}")
    print()


def main():
    tasks = {}

    while True:
        menu()

        user_choice = input("Enter your choice (1-4): ")

        if user_choice == "1":
            add_task(tasks)
        elif user_choice == "2":
            remove_task(tasks)
        elif user_choice == "3":
            mark_complete(tasks)
        elif user_choice == "4":
            view_task(tasks)
        elif user_choice == "":
            print("No input found, Exiting application")
            break
        else:
            print("invalid choice. Enter number between 1-4")

if __name__ == "__main__":
    main()