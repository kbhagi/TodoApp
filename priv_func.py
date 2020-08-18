
class Property:

    def __init__(self, var):
        self.a = var

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2

obj = Property(23)
print(obj.a)


# class AnotherWay:
#
#     def __init__(self, var):
#
#         self.set_a(var)
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self, var):
#
#         if var > 0 and var % 2 == 0:
#             self.__a = var
#         else:
#             self.__a = 2
#
#     #a = property(get_a, set_a)
#
# obj = AnotherWay(28)
# print(obj.a)

# class FinalClass:
#
#     def __init__(self, var=0):
#         self.__set_a(var)
#
#     def __get_a(self):
#         return self.__a
#
#     def __set_a(self, var):
#
#         if var > 0 and var % 2 == 0:
#             self.__a = var
#         else:
#             self.__a = 2
#
#     a = property(__get_a, __set_a)
#
# obj = FinalClass()
# obj.a=6
# print(obj.a)


# class SampleClass1:
#
#     def __init__(self, a):
#         self.set_a(a)
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self, a):
#         if a > 0 and a % 2 == 0:
#             self.__a = a
#         else:
#             self.__a = 2
#
# obj = SampleClass1(16)
#
# print(obj.get_a())