stack = []

def push(item):
    stack.append(item)

def isEmpty():
    if stack == []:
        return True
    else:
        return False


def pop():
    if isEmpty():
        print("Stack underflow")
    else:
        stack.pop()

def display():
        if isEmpty():
            print("stack underflow")
        else:
            print(stack)

if __name__ == '__main__':
    push(1)
    push(2)
    push(3)
    push(4)
    display()
    pop()
    pop()
    pop()
    pop()
    pop()































# creating a empty list to store data
# stack = []
#
#
# # for pushing or adding data to the stack
# def push(num):
#     stack.append(num)
#
# # for removing or deleting data from the stack
# def remove():
#     stack.pop()
#
# # cheacking is the stack is empty or not
# def isEmpty():
#     if stack == []:
#         print("Stack is empty")
#     else:
#         print("Stack is not emtmty")
#
# # getting top of the value from the stack
# def top():
#     print(stack[-1])
#
# def display():
#     # print(stack[::-1])
#     i = len(stack)
#     while i > 0:
#         print(i)
#         i -= 1
#
# if __name__ == '__main__':
#     push(1)
#     push(2)
#     push(3)
#     # display()
#     remove()
#     display()