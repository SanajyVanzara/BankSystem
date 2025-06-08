def tasks_app():
    tasks = []
    task_num = int(input("Enter task number do you want to do : "))
    for i in range(1, task_num+1):
        tasks_name = input(f"Enter your task {i} : ")
        tasks.append(tasks_name)
    print(f"your tasks: {tasks}")

    while True:
        print("Features :\n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit")
        operation = int(input("Enter Feature : "))

        if operation == 1:
            while True:
                add_task = input("Enter task that your want to add : ")
                if add_task not in tasks:
                    tasks.append(add_task)
                    print(f"your task {add_task} successfully added... ")
                    break
                else:
                    print(f"{add_task} already exits...")
        elif operation == 2:
            update_task = input("Enter task that you want to update : ")
            if update_task in tasks:
                new_task = input("Enter new task : ")
                ind = tasks.index(update_task)
                tasks[ind] = new_task
                print(f"{new_task} update on {update_task}")
        elif operation == 3:
            while True:
                del_task = input("Enter task that you want to delete : ")
                if del_task in tasks:
                    ind = tasks.index(del_task)
                    del tasks[ind]
                    print(f"{del_task} successfully deleted...")
                    break
                else:
                    print(f"{del_task} not exits...")
        elif operation == 4:
            print(f"\tyour all tasks : {tasks}")
        elif operation == 5:
            print("\n\tThanks for coming Byy...")
            break
        else:
            print("Enter valid number...")

tasks_app()