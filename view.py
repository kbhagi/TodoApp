import sys


class TaskView:
     def __init__(self):
         pass

     def show_tasks(self):
         tasks = self.db.display_tasks()
         for task in tasks:
             print(task)

     def display_menu(self) -> str:
         print("----------------------------Todo App----------------------------")
         print("""What would you like to do?
         1 - Add Task
         2 - Update a Task
         3 - Delete a Task
         4 - Search a Task""")

     def get_input(self, **kwargs) -> str:
         input_name = kwargs.get("input_name")
         input_name = input(input_name).strip()
         # if not input_name:
         #     input_name = u"\u200B"
         return input_name


def main():
    task_view = TaskView()
    task_view.show_tasks()
