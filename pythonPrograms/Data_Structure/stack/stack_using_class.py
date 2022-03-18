# implementing stack using list
# these are the function that are emplement in stack
#push()
#pop()
#isFull()
#isEmpty()
#display()


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return self.isEmpty()

    def isEmpty(self):
         if self.items == []:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return self.isEmpty()

    def display(self):
        if not self.isEmpty():
            return self.items
        else:
            return self.isEmpty()

if __name__ == '__main__':
    stackItem = Stack()
    stackItem.push(1)
    stackItem.push(2)
    print(stackItem.display())
    stackItem.pop()
    stackItem.pop()
    print(stackItem.display())




