# from task_model import Task
from pathlib import Path
import os

from task_model import Task
class DB:
    def __init__(self, file_name=None, path=None):
        print(file_name)
        self.file_name = file_name
        self.path = path
        self.absolute_path = self.path + self.file_name
        print(self.absolute_path)
        self.initialize(self.path, self.absolute_path)
        print("printing __init__", self.file_name)
        print(self.file_name)
        #self._data = data
        # self.append_file = self.append_to_file(self._file_name,self._data)

    def __str__(self):
        return f'{self.file_name}'

    @property
    def file_name(self):
        print("calling getter for file_name")
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        if not value:
            raise Exception("File name cannot be None or Empty")
        self._file_name = value

    @property
    def path(self):
        print("calling getter for path")
        return str(self._path)

    @path.setter
    def path(self, value):
        if not value:
            raise Exception("Path cannot be None or Empty")
        self._path = value


    def check_file_exists(self, path_name, absolute_path):
        path = Path(path_name)
        file_path = Path(absolute_path)
        print("Path name")
        print(path.name)
        path_status = path.exists()
        file_status = file_path.is_file()
        return path_status, file_status


    def create_directory(self, path):
        os.makedirs(path)


    def touch_file(self, absolute_path):
        with open(absolute_path, 'a'):
            os.utime(absolute_path, None)

    def read_file(self):
        with open(self.absolute_path, 'r') as readfile:
            contents = readfile.read().split(":")
            read_task_data = list(filter(None, contents))
            return read_task_data


    def search_task(self, task):
        existing_tasks = self.read_file()
        print("tasks read")
        print(existing_tasks)
        for index, task_data in enumerate(existing_tasks):
            if task_data:
               items = task_data.split(",")
               if items:
                  taskobject = Task(items[0], items[1], items[2], items[3])
               if taskobject.name == task.name:
                  print("Task found at :", index)
                  return existing_tasks, index, taskobject
        print("Task not found ")

    def update_task(self, task):
        # contents = task.__dict__
        print("update task contents")
        # read_task_data = self.read_file()
        result = self.search_task(task)
        if result:
            read_task_data, index, task_object = result
            if index and task_object:
                existing_task = read_task_data[index]
                new_task = existing_task.split(",")
                if existing_task:
                    new_task[0] = task.name
                    new_task[1] = task.description
                    new_task[2] = task.log_date
                    new_task[3] = task.status
                    read_task_data.remove(existing_task)
                    print("read_task_data after removing existing task")
                    print(read_task_data)
                    read_task_data.insert(index, ','.join(new_task))
                    self.save_task(read_task_data)
        else:
            return "Tasks db is empty"

    def delete_task(self, task):
        # existing_data = self.read_file()
        result = self.search_task(task)
        print("result of search task", result)

        if result:
            existing_tasks, index, taskobject = result
            print(existing_tasks, index , taskobject)
            if existing_tasks:
                task_to_delete = existing_tasks[index]
                print("index of task to be deleted", task_to_delete)
                print(task_to_delete)
                if task_to_delete:
                    print("task_to_delete", task_to_delete)
                    existing_tasks.remove(task_to_delete)
                    self.save_task(existing_tasks)
                    return "Task deleted"
                else:
                    return "task to delete is None or empty"
            else:
                return "existing task not found"

        else:
            return "Task not found"

    def add_task(self, task):
        data = task.name + ','+task.description+','+task.log_date + ',' + task.status + ':'
        with open(self.absolute_path, 'a') as appendFile:
            appendFile.write(data)
        return "appended to file"

    def save_task(self, tasks):
        #print(tasks.__dict__)
        with open(self.absolute_path, 'w') as writefile:
            for task in tasks:
                writefile.write(task+':')
            # writefile.write(str(tasks))
    #
    def initialize(self, path_name, absolute_path):
        path_status, file_status = self.check_file_exists(path_name, absolute_path)
        if path_status and file_status:
            return
        if not path_status:
            self.create_directory(self.path)
        if not file_status:
            self.touch_file(absolute_path)

# class TaskEncoder(object):

