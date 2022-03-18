# # creating a class employee
# class employee:
#     # class variable same for all the instances ( objects )
#     Company = "Google"
#
#     def __init__(self, name, age, position):
#         # instance variable different for different instances.
#         self.name = name
#         self.age = age
#         self.position = position
#
#     # class method
#     def get_details(self):
#         return f"My name is {self.name} and i am {self.age} year old and i am a {self.position} at {self.Company}. "
#
#
# # creating an object and passing argument and it taken by init() method automatically
# emp1 = employee("John", 22, "Software Developer")
#
# emp2 = employee("Asif", 22, "Web Developer")
#
# print(emp1.get_details())
# print(emp2.get_details())

#--------------------------------- Access Specifier--------------------------------------
# class public:
#     # this is public class variable
#
#     Company = "Google"
#
#     # constructor
#     def __init__(self, name, age):
#         # this is public instance variable
#         self.name = name
#         self.age = age
#
#     # this is public method
#     def get_details(self):
#         return f"My name is {self.name} and i am {self.age} year old"
#
#
# # creating an object or intace for the same class
# p1 = public("Asif", 20)
#
# #accessing the public instance variable
# print(p1.age)
#
# # accessing the public method
# print(p1.get_details())
#
# # accessing the public class variable
# print(p1.Company)

#-------------------------------------------------- protected --------------------------------------
# class protected:
#
#     #defining a protected class variables with a single ( _ ) underscore
#     _salary = '50k'
#
#     def __init__(self,name):
#
#         #protected instance variable
#         self._name = name
#
#     # protected instance method
#     def _details(self):
#
#         # accessing the protected instance and class variables
#         return f"My name is {self._name} and my salary is {self._salary}"
#
# pro1 = protected("Emplpoyee")
#
# print(pro1._salary)
#
# #accessing the intance method you cannot directy access without single underscore
# print(pro1._details())

#--------------------------------Private--------------------------------
# class students:
#
#     __class_teacher = "Alex Miller"
#
#     def __init__(self,name,branch):
#         self.__name = name
#         self.__branch = branch
#
#     def __protected_details(self):
#         print(f"My name is {self.__name} and i'm from {self.__branch} and my class teacher is {self.__class_teacher}")
#
#     def get_details(self):
#         return self.__protected_details()
#
# st1 = students("john","B.C.A")
#
# print(st1.get_details())
#
# print(st1.__protected_details)
#
#----------------class variable and instance variable ------------------------
# class employee:
#
#     #this is class variable
#     Company = "Google"
#
#     def __init__(self,name,age,salary):
#         #these are instance variables
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def get_details(self):
#         return f"Name is {self.name}, Age is {self.age}, Salary is {self.salary} , Company is {self.Company}"
#
#
# emp1 = employee("Mark",20,"30k")
# print(emp1.get_details())
#
#
# emp2 = employee("Tim",22,"50k")
# print(emp2.get_details())
#
# print("After changing the Instance and Class Variable")
#
# employee.Company = "Facebook"
#
# emp1.name = "Mark Zukerberg"
#
# emp1.salary = "100k"
#
# print(emp1.get_details())
#
# #changing the name of emp1 will not affect the emp2
# # but changing the class variable company its affect all the instances
# print(emp2.get_details())

#-------------------------instance method and class methods---------------------
# class students:
#
#     no_of_students = 0
#
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         students.no_of_students += 1
#
#     def get_details(self):
#         return f"Name is {self.name} and roll number is {self.rollno}"
#
#     @classmethod
#     def count_students(cls):
#         return cls.no_of_students
#
#
# stud1 = students('Asif',12345)
#
# stud2 = students("skillf",6789)
#
# print(stud1.get_details())
#
# print(stud2.get_details())
#
# print(students.count_students())

#---------------------------------class method as an alternative constructor-----------------------
# class dates:
#
#     def __init__(self,day,month,year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def print_date(self):
#         return f"{self.day}/{self.month}/{self.year}"
#
#     @classmethod
#     def get_dates(cls,date):
#        day, month, year = date.split('-')
#        return cls(day,month,year)
#
# d1 = dates("10","02","2021")
# d2 = dates.get_dates("02-10-2001")
#
# print(d1.print_date())
# print(d2.print_date())

# class employee:
#
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def get_details(self):
#         return f"Name is {self.name} age is {self.age} and salary is {self.salary}"
#
#     @classmethod
#     def get_employee_details(cls,details):
#         name, age, salary = details.split('-')
#         return cls(name, age, salary)
#
# emp1 = employee("John",23,"50k")
# emp2 = employee.get_employee_details("Ram-35-50k")
#
# print(emp1.get_details())
# print(emp2.get_details())

#--------------------------------------Static method----------------------------
# class calculation:
#
#     # Creating a static method for finding square of any number
#     # @staticmethod
#     def find_sqr(num):
#         return num * num
#
#     # creating a static method for finding the cube of any method
#     # @staticmethod
#     def find_cube(num):
#         return num*num*num
#
# calculation.find_sqr = staticmethod(calculation.find_sqr)
# calculation.find_cube = staticmethod(calculation.find_cube)
#
# print(calculation.find_cube(3))
#
# print(calculation.find_sqr(4))

#-----------------------dunder methods or magic methods and overloading ---------------------------
# those method which starts __ double under score and ends with double underscores are called dunger or magic methods.
# these methods are special methods. there are soo many dunder/magic methods .but in this totorial we will going to see some important  methods that are
# are going to use regulary
# __init__(self) :- As we arelady know about __init__(self) and also its works ___it is basically a constructor. Constructor means
# when the objects is it is automatically called.
# ex - __str__(self), __repr__(self), __init__(self), __add__(self), __sub__(self), __mul__(self)
# __str__(self) :- This will use to print the string in a format that understand by the users it will call when the obj is created
# __repr__(self):- representation of the object this is also same as str method but this is basically use while debugging.it exatally work as same like __str__(Self) method
# __add__(self) :- this method is use to add two valuse ( like it can be integer float or string) this is use to do overloading
# __len(self) :- this method is use to find the length of a string or length of a list
# class example:
#
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city
#
#     def __str__(self):
#         return f"My name is {self.name} and i live in {self.city}"
#
#     def __repr__(self):
#         return f"example('{self.name}','{self.city}')"
#
#
#
# ex1 = example("asif","lucknow")
#
#
# print(ex1.__str__())
# print(ex1.__repr__())
# # this is the another method to call it does the same thing
# print(str(ex1))
# print(repr(ex1))
#
# #---------------------------overloading---------------------
# operator overloading means using same operator for different use like add to numbers or add two string
# class calculation:
#
#     def __init__(self,num1):
#         self.num1 = num1
#
#     def __add__(self, other):
#         return self.num1 + other.num1
#
#     def __sub__(self, other):
#         return self.num1 - other.num1
#
#     def __mul__(self, other):
#         return self.num1 + other.num1
#
#     def __len__(self):
#         return len(self.num1)
#
#
#
#
# n1 = calculation(43)
# n2 = calculation(54)
#
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
#
# # This is also use for string
# s1 = calculation("Hello")
# s2 = calculation("World")
# print(s1 + s2)
#
# #now len is use the find the length of objects
#
# f1 = calculation("this is a string")
#
# print(len(f1))

# ------------------------------------------ property decorator or setter --------------------
# it is allow to access to use attributes without setting getter and setter every where
# class students:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#
#     @property
#     def email(self):
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @property
#     def fullname(self):
#         return f"{self.fname} {self.lname}"
#
#     # setter is use to change the atttribute of objects at run time
#     @fullname.setter
#     def fullname(self,name):
#         self.fname, self.lname = name.split(' ')
#
#     @fullname.deleter
#     def fullname(self):
#         print("Name is deleted")
#         self.fname = None
#         self.lname = None
#
# stud1 = students('web', "dev")
#
# stud1.fullname = "Mohammad Asif"
#
# del stud1.fullname
#
# print(stud1.fname)
# print(stud1.lname)
# print(stud1.email)

# class hello:
#
#     def print_hello(self):
#         return "Hello world !"
#
#     @property
#     def print_string(self):
#         return "This method is define with property decorator"
#
#
# str1 = hello()
#
# print(str1.print_hello())
#
# print(str1.print_string)


# str = "This is \\ a string"
# print(str)


i = 0  # initializing the i before starting loop
while i <= 10:  # i will go for from 0 to 10 until the condtion become False
    print("Codeupon")  # printing the name
    i += 1  # increment the value of i by 1

# (+) is operator and, a and b are operands on which operation are perform
a = 5
b = 4
c = a + b
print(c)