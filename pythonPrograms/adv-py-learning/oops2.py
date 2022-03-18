# -----------------------Method overiding and method overloading---------------------

#--------Dunder method(magic method) : -  Those method whose name are starting with double underscore (__) and ends with
# double underscore (__) are called dunder method or magic method ( ex- __init__, __str__, __repr__, __add__ etc)

# ----------------------------------Method overloading----------
# class A:
#
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def __str__(self):
#         return f"{self.num1} ,{self.num2}"
#
#     def __add__(self, other):
#         s1 = self.num1 + other.num1
#         s2 = self.num2 + other.num2
#         return s1, s2
#
#     def __sub__(self, other):
#         s1 = self.num1 - other.num1
#         s2 = self.num2 - other.num2
#         return s1, s2
#     def __truediv__(self, other):
#         s1 = self.num1 / other.num1
#         s2 = self.num2 / other.num2
#         return s1,s2
#
# s1 = A(29, 15)
# s2 = A(43, 85)
#
# print("---Adding---")
# print(s1)
# print(s2)
# s3 = s1 + s2
# print(s3)
#
# print("---Subtracting---")
# print(s1)
# print(s2)
# s3 = s1 - s2
# print(s3)
#
# print("---Division---")
# print(s1)
# print(s2)
# s3 = s1 / s2
# print(s3)




#----------------------------super fucntion------------------------------------------
# 1 using with constructor
# class person:
#
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
# class student(person):
#
#     def __init__(self,name,age,profession):
#         super(student, self).__init__(name,age)
#         self.profession = profession
#
#     def get_details(self):
#         return f"Name - {self.name} , Age - {self.age} , Profession - {self.profession}"
#
# stud1 = student("Skillf",18,"student")
# print(stud1.get_details())

#2--------class property------------------------
# class vehicle:
#     milage = 50
#
#
# class car(vehicle):
#     milage = 30
#
#     def get_details(self):
#         #accessing the milage of vehicle class  or base class we use super() function
#         print(f"Milage of the average vehicles are {super().milage}")
#
#         #accessing the milage of car class or self class we use self keyword
#         print(f"Milage of average cars are {self.milage}")
#
#
# c1 = car()
# c1.get_details()

#------------------------------------accessing the base class method using super------------
# base class
# class employee:
#
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     # base method
#     def emp_details(self):
#         return f"Name - {self.name}, Age - {self.age}"
#
#
# # derived class from employee
# class programmer(employee):
#
#     # accessing the base constructor for name and age using super
#     def __init__(self,name,age,language):
#         super(programmer, self).__init__(name,age)
#         self.language = language
#
#     # this is derived class method but we also access the base class method using super
#     def prog_details(self):
#         text = super().emp_details()
#         return text + f", Language is {self.language}"
#
#
# prog1 = programmer("Skillf",24,"Python")
#
# print(prog1.prog_details())
#------------------------------------------------------------------------------------------------------
# --------------------------Abstract base class and abstract base method---------------

# abstract base class --> A class is called Abstract class if its contains one or more abstract method. An Abstract
# method is a methods only declaration with no implementation ..Basically abstract class is a  blue print for all the classes

# -------------------------without abstract method------------------------------
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")




d = Human()



print(d.move())


#--------------------------with abstract method -------------------------------------
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Human(Animal):
#
#     def move(self):
#         print("I can walk and run")
#
#
# class Snake(Animal):
#     def move(self):
#         print("I can crawl")
#
#
# class Dog(Animal):
#     def move(self):
#         print("I can bark")
#
#
# class Lion(Animal):
#     def move(self):
#         print("I can roar")
#
#
# d = Human()
# print(d.move())
#--------------------------------------------------------------

# from abc import ABC, abstractmethod
#
# class shape(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class circle(shape):
#
#     def __init__(self,radius):
#         self.radius = radius
#
#     def print_area(self):
#         area = 3.14*(self.radius*self.radius)
#         return area
#
# obj1 = circle(3)
# print(obj1.print_area())