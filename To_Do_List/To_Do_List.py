# concept to create a to do list where user can add, update and delete tasks and save the list in a flie.
# focus :- File handeling ,CLI, and basic object oriented programming.
tasks=[]
print("Welcome to To-Do-List! Plan your day with us")
while True:
    print("====To-Do-List====")
    print("1. Add Tasks: ")
    print("2. View Tasks: ")
    print("3. Update Tasks: ")
    print("4. Delete Tasks: ")
    print("5. Exit: ")
    try:
        choice = int(input("Enter your choice:"))
        print("You enterned:", choice)
        if choice==1:
            print("Add Tasks")
            task=input("Enter Your task:")
            tasks.append(task)
            print("Task Added Successfully!")
        elif choice ==2:

            if len(tasks) == 0:
                print("Add tasks first!")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
        elif choice ==3:
            if len(tasks)==0:
                print("Add tasks first")
            else:
                print("\n Your tasks")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}, {task}")
                task_number=int(input("Enter task number here!"))
                if 1<=task_number<=len(tasks):
                    new_task=input("enter your new task here!")
                    tasks[task_number-1]=new_task
                    print("tasks updated successfully!")
                else:
                    print("Invalid task number")
        elif choice==4:
            if len(tasks)==0:
                print("first add some tasks")
            else:
                print("\n your tasks")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                tasks_number= int (input("Enter task number here you wanna delete~"))
                if 1<=tasks_number<=len(tasks):
                    deleted_task= tasks.pop(tasks_number-1)
                    print(f"Deleted task: {deleted_task}")
                    print("task deleted successfully!")
        elif choice==5:
            print("Thanks! Have a Good Day")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number!")