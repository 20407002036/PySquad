# while, input , if
# 1 Add task, 2 view tasks, Remove, 4 Quit

from tasks import Tasks
print("Welcome.")
print("Help Menu")
print("1. Add task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Quit")

while True:
    choice = input("Enter you choice (Either 1,2,3,4): ")


    if choice == "1":
        # call the class, create task function
        task_Name = input("Enter name of task: ")

        Tasks.add_task(task_Name)


    elif choice == "2":
        # call the class, View tasks
        Tasks.view_tasks()

    elif choice == "3":
        # call class, remove task
        pass

    elif choice == "4":
        # close the program
        pass

    else:
        # default when user enters value not 4 - 1
        print("Value must be 1,2,3 or 4")
        break
