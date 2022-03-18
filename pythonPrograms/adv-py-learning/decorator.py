#-----------------Decorator----------------------
# Decoration is a very powerful to change the behaviour of any existing fuction without make any change to it at compile time.
# We can pass a function into a function and create a function inside a fucntion and return a function ..yes you will not understand this line lates
# check an example to understand

# def division(a,b):
#     return a/b
#
# def new_div(func):
#
#     def swap(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return swap
#
# div2 = new_div(division)
# print(div2(2,4))
#

# another example
def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function()

outer_function()

# or

def outer_function():
    message = "Hi"

    def inner_function():
        print(message)
    return inner_function

name = outer_function()
name()