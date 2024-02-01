class ToDoList:
    """
    deal with the core components of a to-do: init -> initialization

    [] lists. append , view, remove
    """

    def __init__(self):
        """
        This is our init function that initializes the base functions of out to-do
        :return:
        """
        self.tasks = []

    def add_task(self, task):
        """
        By the help of the append fuction in list we add an item to the existing list
        :param task:
        :return:
        """
        self.tasks.append(task)

        print(f"The task {task} has been created")


    def view_tasks(self):
        # give the items in the list
        if not self.tasks:
            print("No to-do's at the moment")

        else:
            print("Here is the list of to-do's")

            for index, task in enumerate(self.tasks, start=1):
                """
                Defining a index, variable.
                enumwarate loop through. 
                task list.start at 1st value
                """
                print(f"{index}.{task}")
                # 1. program
                # 2. Homework

    def remove_task(self, task_index):
        """
        This function will remove an alredy existing task based on its index in the lists
        Will use the pop faction to pop the task.

        :return:
        """
        if 1<= task_index<= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task {removed_task} removed \n")

        else:
            print("Invalid task index")
