# To - Do List Application
tasks = []
def show_menu():
    print("\n===== To-Do LIST MENU =====")
    print("1. Add Task")
    print("2. view Task")
    print("3. Remove TAsk")
    print("4. Exit")
while True:
    show_menu()
    choice = input("Enter your choice: ")

    #Add Task
    if choice == '1':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")
        
    #view Task
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(task, start=1):
                print(f"{i}.{task}")

    #Remove Task
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nTask")
            for i, task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed successfully!")
            except:
                print("Invalid task number.")

        #Exit
    elif choice == '4':
        print("Exiting To-Do List App...")
        break

    else:
        print("Invalid choice.please try again.")    



    

