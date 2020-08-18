# import json
# import datetime
# import DB
# from json import JSONEncoder
#FILE_NAME = 'db.json'


class Task(object):
    # tasks = []
    # items = {}
    def __init__(self, name=None, description=None, log_date=None, status=None):
        self.name = name
        self.description = description
        self.log_date = log_date
        self.status = status
        # self.set_name(name)
        # self.set_description(description)
        # self.set_log_date(log_date)
        # self.set_status(status)

    @property
    def name(self):
        print("@property getter name called")
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def log_date(self):
        return self._log_date

    @property
    def status(self):
        return self._status

    @name.setter
    def name(self, value):
        print("@name setter class method called")
        if not value or value.isspace():
            raise Exception("Name cannot be none or empty")
        self._name = value

    @description.setter
    def description(self, value):
        print("@description setter class method called")
        if not value or value.isspace():
            raise Exception("description cannot be none or empty")
        self._description = value

    @log_date.setter
    def log_date(self, value):
        print("@log_date setter class method called")
        if not value or value.isspace():
            raise Exception("log_date cannot be none or empty")
        self._log_date = value

    @status.setter
    def status(self, value):
        print("@status setter class method called")
        if not value or value.isspace():
            raise Exception("status cannot be none or empty")
        self._status = value


    # def set_name(self, var):
    #     if var:
    #         self.__name = var
    # def set_description(self, var):
    #     if var:
    #         self.__name = var
    # def set_log_date(self, var):
    #     if var:
    #         self.__log_date = var
    # def set_status(self, var):
    #     if var:
    #         self.__status = var
    # def get_name(self):
    #     return self.__name
    # def get_description(self):
    #     return self.__description
    # def get_status(self):
    #     return self.__status
    # def get_log_date(self):
    #     return self.__log_date




#obj.name = "aa"
# obj.description = "Coding"
# obj.log_date = datetime.date.today().__str__
# obj.status = "In Progress"
#print(obj.name)




