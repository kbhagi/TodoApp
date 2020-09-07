import sys

from task_model import Task
from DB import DB
import datetime

# from view import TaskView
from view import TaskView

FILE_NAME = 'db.json'
PATH = 'E:/BuildStuff/TodoApp/a/'

class TodoController:
    def __init__(self, file_name, path):
        self.view = TaskView()
        # self.taskmodel = Task()
        self.db = DB(file_name, path)

    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, val):
        if val:
            self._db = val

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, val):
        if val:
            self._view = val

    def add_tasks(self, **kwargs):
        tasks = kwargs.get("tasks_list")
        print("tasks input")
        print(tasks)
        for task in tasks:
            self.db.add_task(task)
        return True

    # def handle_add(self):


    def start_program(self, **kwargs):
        choice = kwargs.get("choice")
        print("choice ")
        print(choice)
        while choice.lower() != "q":
            print("Adding a Task")
            # choice = input(">")
            if choice == "1":
                task_name = self.view.get_input(input_name="task name: ")
                task_description = self.view.get_input(input_name="task description: ")
                task_date = datetime.date.today().__str__()
                task_status = self.view.get_input(input_name="task status: ")
                task = Task(task_name, task_description, task_date, task_status)
                tasks_list = [task]
                self.add_tasks(tasks_list=tasks_list)
                break

            elif choice == "2":
                print("Updating a Task")
                task_name = self.view.get_input(input_name="task name: ")
                task_description = self.view.get_input(input_name="task description: ") or "default"
                print("task description")
                print(task_description)
                task_date = "default" #datetime.date.today().__str__()
                task_status = self.view.get_input(input_name="task status: ") or "default"
                print(task_status)
                task = Task(task_name, task_description, task_date, task_status)
                print("task log_date")
                print(task.log_date)
                result = self.db.update_task(task)
                print("result of updating at ask")
                print(result)
                break

            elif choice == "3":
                print("Searching a task")

                break

            elif choice == "4":
                print("Deleting a Task")
                break

            else:
                print("Sorry, I didnt recognize that option")
                print("none of option matched")
                self.view.display_menu()
                choice = self.view.get_input(input_name="choice")
        print("Thank you! Shutting down.")
        sys.exit
        print("exiting start_program")

        # task_controller.add_tasks(tasks_list=tasks_list)


def main():

    # task = Task("Code", "Add a view to a Todo App", datetime.date.today().__str__(), "In-Progress")
    # task1 = Task("Read", "Read The Coding Career Handbook written by Shawn Swyx Wang", datetime.date.today().__str__(),
    #              "To-do")
    # task2 = Task("Learn", "Solve problems from AlgoExpert", datetime.date.today().__str__(), "To-do")
    # task3 = Task("DRBot", "Work on adding SQS to DR Bot", datetime.date.today().__str__(), "To-do")
    # task4 = Task("CDK", "Write CDK to setup LB's,Security Groups,Subnets ,VPC,IG,Route Table",
    #              datetime.date.today().__str__(), "To-Do")
    # # data_manager1 = DB(FILE_NAME)
    # print("data manager")
    # print(db)
    # tasks = {}
    # tasks_list = [task, task1, task2, task3, task4]

    # contents = db.read_file()
    # print("--------------old contents----------------")
    # print(contents)
    # index , task = db.search_task(task1)
    # print(task.__dict__)
    # task2 = Task("Eat", "Learn to cook veg food", datetime.date.today().__str__(), "Completed")
    # result = db.update_task(task2)
    # print("result of updating at ask")
    # print(result)
    # contents = db.read_file()
    # print("--------------new contents----------------")
    # print(contents)
    # delete_status = db.delete_task(task2)
    # print("result of deleting a task", delete_status)
    # result = db.read_file()
    # print("------------------contents after deleting---------------")
    # print(result)
    task_controller = TodoController(FILE_NAME, PATH)
    task_controller.view.display_menu()
    option = task_controller.view.get_input(input_name="choice > ")
    task_controller.start_program(choice=option)
    print("entering main")


    # print(result)

    # # data_manager.append_to_file(FILE_NAME,data)


if __name__ == '__main__':
    main()
