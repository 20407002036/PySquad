# while, input , if
# 1 Add task, 2 view tasks, Remove, 4 Quit

from tasks import ToDoList

todo_list = ToDoList()

print("Welcome.")
print("Help Menu")
print("1. Add task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Quit")
print("Enter you choice (Either 1,2,3,4): ")

while True:
    choice = input(">_ ")
    if choice == "1":
        # call the class, create task function
        task_Name = input("Enter name of task: ")

        todo_list.add_task(task_Name)

    elif choice == "2":
        # call the class, View tasks
        todo_list.view_tasks()
    elif choice == "3":
        # call class, remove task
        task_index = int(input("Enter task index to be removed: "))
        # From the terminal the program receives strings, we have to convert this to int by type casting.
        todo_list.remove_task(task_index)

    elif choice == "4":
        # close the program
        print("Bye!!...")
        break
    else:
        # default when user enters value not 4 - 1
        print("Value must be 1,2,3 or 4")
        pass
