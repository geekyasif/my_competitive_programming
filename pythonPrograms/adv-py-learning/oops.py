# Class and objects
# In this example we learn about how to make class objects,attributes and methods
# class student:
#     branch1 = "Bca"
#     career = "software Developer"
#
#     def details(self):
#         print("I,m student of ",self.branch1," at integral university and want to be a ",self.career)
#
# stud1 = student()
# print(stud1.details())

# class Employee:
#     company = "Google"
#     salary = "30k"
#
#     # @staticmethod
#     # def users():
#     #     print("Hello users")
#
#     def getSalary(self):
#         print("Work at ",self.company," Salary is ",self.salary)
#
# dev = Employee()
# dev.salary = "50k"
# print(dev.getSalary())

#---------------------Constructor in Python class _-----------------
# class employee:
#
#     def __init__(self,name,salary,company):
#         self.name = name
#         self.salary = salary
#         self.company = company
#
#     def getDetails(self):
#         print("Name is ",self.name," Salary is ",self.salary," And Company is ",self.company)
#
# class programmer(employee):
#
#     def __init__(self,name,salary,company,langauge):
#         self.langauge = langauge
#         super(programmer, self).__init__(name,salary,company)
#
#     def display(self):
#         print(f"NAme is {self.name} salary is {self.salary} company is {self.company} and language is {self.langauge}")
#
#
#
# dev = employee("Asif","50k","Amazon")
# # print(dev.getDetails())
# dev2 = programmer("dev2","400k","Google","cpp")
# print(dev2.display())

# import abc
# class Shape(metaclass=abc.ABCMeta):
#    @abc.abstractmethod
#    def area(self):
#       pass
# class Rectangle(Shape):
#    def __init__(self, x,y):
#       self.l = x
#       self.b=y
#    def area(self):
#       print(self.l*self.b)
#
#
# r = Rectangle(10,20)
# print (r.area())
# print("hello \n asif \n ka ")
#--------------------------------------miltiple construtction-----------------
# class emplyee:
#     def __init__(self,name,id):
#         self.name= name
#         self.id = id
#
#     def emplyeeDetails(self):
#         print(self.name, self.id)
#
# class player:
#
#     def __init__(self,game):
#         self.game = game
#
#     def getGame(self):
#         print(self.game)
#
# class programmer(emplyee,player):
#
#     def __init__(self,name,id,game,language):
#         self.name = name
#         self.id =  id
#         self.game = game
#         self.language = language
#
#     def getProgDetails(self):
#         print(self.name,self.id,self.game,self.language)
#
# a = emplyee("asif",123)
# b = player("Football")
# a.emplyeeDetails()
# b.getGame()
#
# c = programmer("name","id","game","laguage")
# c.getProgDetails()

#------------------------multilevel inheritance------------------
# class GrandFather:
#
#     def grandDetails(self):
#         print("Im grandfather")
#
# class Father(GrandFather):
#
#     def fatherDetails(self):
#         print("Im father")
#
# class Son(Father,GrandFather):
#
#     def sonDetails(self):
#         print("im son ")
#
# a = GrandFather()
# a.grandDetails()
# b = Father()
# b.fatherDetails()
# c = Son()
# c.grandDetails()

#------------------------Access specifier ------------------
# class a:
#     public_variable = "This is a public variable and access by any class and instance variable"
#     _protectedVariable = "This is protected variable and it only can be access through derived class and instance of the class"
#     __privateVariables = "This can only access by instance of the variable but sytax of calling is (__a__privateVariables)"
#
#
# b = a()
# print(b.public_variable) # calling public variable
# print(b._protectedVariable) # calling protected variable
# print(b.__a__privateVariables) # calling private variable
#---------------------------------------------property setter getter and deleter decorator-----------------------------
# class a:
#
#     @property
#     def hello(self):
#         return "You can call this method without () this if you use property method @property"
#
# b = a()
# print(b.hello)
# class employee:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     @property
#     def email(self):
#         return f"{self.fname}.{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self,string):
#         names = string.split("@")[0]
#         self.fname = names.split('.')[0]
#         self.lname = names.split('.')[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
# asif = employee("md","asif")
# print(asif.email)
# asif.email = "asif.md@gmail.com"
# print(asif.email)
# del asif.email
# print(asif.email)
# asif.email = "md.asif08737@gmail.com"
# print(asif.email)

#-----------------------------------------Revision OOPs Python ----------------------------------------------------
# class person:
#     amount = 0
#     def __init__(self,name):
#         self.name = name
#         person.amount +=1

    #str method converted the object into string --- When you create an object and pass the argument to the constructor
    #and you simply print the instace object it will return and object instead of any string ....So we created a str method
    # that converted the object into string and return and now when you print the instance you will get a string.
#     def __str__(self):
#         return f"My name is {self.name}"
#
#     def __del__(self):
#        person.amount -= 1
#
# p1 = person("Mohammad Asif")
# p2 = person("Mohammad IRshad Akram")
# del p2
# print(p1)
# print(person.amount)

#--------------------------------Super and overriding---------------
# class A:
#
#     def __init__(self):
#         self.varA = "This is varA"
#     def __str__(self):
#         return self.varA
#
# class B(A):
#
#     def __init__(self):
#         super().__init__()
#         self.varB = "This is varB"
#
#     def __str__(self):
#         return self.varB
# a = A()
# print(a)
# b = B()
# print(b.varB)

# Python example to show that base
# class members can be accessed in
# derived class using super()
# class Base(object):
#
#     # Constructor
#     def __init__(self, x):
#         self.x = x
#
#
# class Derived(Base):
#
#     # Constructor
#     def __init__(self, x, y):
#         ''' In Python 3.x, "super().__init__(name)"
#             also works'''
#         super(Derived, self).__init__(x)
#         self.y = y
#
#     def printXY(self):
#         # Note that Base.x won't work here
#         # because super() is used in constructor
#         print(self.x, self.y)
#
#     # Driver Code
#
#
# d = Derived(10, 20)
# d.printXY()


class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"name is {self.name} and id is {self.id}"

class Teacher(Employee):

    def __init__(self, name, id, lang):
        super(Teacher, self).__init__(name, id)
        # Employee.__init__(self, name, id)
        self.lang = lang

    def __str__(self):
        text = super(Teacher, self).__str__()
        text += f" and i teaches {self.lang}"
        return text



emp1 = Employee("asif",123)
T1 = Teacher("haris", 1231, "kdksd")
print(T1)

# class Animal():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("I am", self.name, "and I am", self.age, "years old")
#
#
# class Dog(Animal):
#
#     def __init__(self, name, age, breed):
#         super(Dog,self).__init__(name, age)  # This will call the Animal classes constructor method
#         self.breed = breed
#
#     def speak(self):
#         print("I am a Dog")
#
#
# t = Animal("i",8)
#
# tim = Dog("Tim", 5, "local Dog")
# tim.speak()  # This will print "I am a Dog"