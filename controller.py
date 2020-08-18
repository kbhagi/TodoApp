from task_model import Task
from DB import DB
import datetime

FILE_NAME = 'db.json'
PATH = 'E:/BuildStuff/TodoApp/a/'

class TodoController:
    def __init__(self):
        pass



    db = DB(FILE_NAME, PATH)
    task = Task("Code", "Build a Todo App", datetime.date.today().__str__(), "In-Progress")
    task1 = Task("Pray", "Do a ritual", datetime.date.today().__str__(), "Completed")
    task2 = Task("Eat", "Chew food", datetime.date.today().__str__(), "Completed")
    # # data_manager1 = DB(FILE_NAME)
    # print("data manager")
    # print(db)
    db.add_task(task)
    db.add_task(task1)
    db.add_task(task2)
    contents = db.read_file()
    print("--------------old contents----------------")
    print(contents)
    # index , task = db.search_task(task1)
    # print(task.__dict__)
    # task2 = Task("Eat", "Learn to cook veg food", datetime.date.today().__str__(), "Completed")
    # result = db.update_task(task2)
    # print("result of updating at ask")
    # print(result)
    # contents = db.read_file()
    # print("--------------new contents----------------")
    # print(contents)
    delete_status = db.delete_task(task2)
    print("result of deleting a task", delete_status)
    result = db.read_file()
    print("------------------contents after deleting---------------")
    print(result)


    # # data_manager.append_to_file(FILE_NAME,data)