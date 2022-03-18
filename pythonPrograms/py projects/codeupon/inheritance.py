# ----------------------------single level inheritacnc------------------------
# class A:
#     # base class
#
# class B(A):
#     #derived class from class

#--------------Example of single inheritance------------------

# class person:
#
#     def __init__(self,profession,organization):
#         self.profession = profession
#         self.organization = organization
#
#     def get_details(self):
#         return f"{self.profession} at {self.organization}"
#
# class student(person):
#
#     def get_details(self):
#         return f"{self.profession} at {self.organization}"
#
# p1 = person("Employee","Microsoft")
# print(p1.get_details())
# s1 = student("Student","Integral University")
# print(s1.get_details())


#---------------------------------------------Overriding
# class employee:
#
#     company = "Google"
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def get_details(self):
#         return f"My name is {self.name} and age is {self.age} and a normal employee"
#
# class programmer(employee):
#
#     # overiding the compnay means changing the value
#     company = "Facebook"
#
#     language = "Python"
#
#     def get_details(self):
#         return f"Name is {self.name} age is {self.age}, i'm a {self.language} developer and my company is {self.company}"
#
#
# emp1 = employee("John",21)
# print(emp1.get_details())
#
# prog1 = programmer("Asif",20)
# print(prog1.get_details())

#-----------------------------multilevel inheritance------------------------
# class grand_father:
#
#     def get_details(self):
#         return "I am grandfather"
#
# class dad(grand_father):
#     pass
#
# class son(dad):
#     pass
#
# obj2 = grand_father()
# obj3 = dad()
# obj1 = son()
#
# print(obj1.get_details())

#---------------------------------multiple inheritance------------------------------
class employee:

    name =""
    age = ""

class player:
    game = ""

class programmer(employee,player):

    def get_details(self):
        return f"Name is {self.name}, age is {self.age}, and i love playing {self.game}"


prog1 = programmer()
prog1.name = "John"
prog1.age = "21"
prog1.game = "Cricket"

print(prog1.get_details())
