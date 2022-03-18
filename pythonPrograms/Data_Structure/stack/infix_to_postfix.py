class Stack:

    def __init__(self):
        self.stack = []
        self.postfix_exp = ""

    def atTop(self):
        print(self.stack[-1])

    def isEmpty(self):
        if self.stack is None:
            return True
        else:
            return False

    def isOperator(self, c):
        if c == "+" or c == "-" or c == "*" or c == "/":
            return True
        else:
            return False

    def precedence(self, c):
        if c == "^":
            return 3
        elif c == "*" or c == "/":
            return 2
        elif c == "+" or c == "-":
            return 1
        else:
            return -1

    def insert(self, infix_exp):
        for i in infix_exp:
            if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
                self.postfix_exp += i
            elif i == "(":
                self.stack.append(i)
            elif i == ")":
                while (self.atTop() != "(") and (not self.isEmpty):
                    poped_operator = self.atTop()
                    self.postfix_exp = poped_operator
                    self.delete()
            elif self.isOperator(i):
                if self.isEmpty():
                    self.stack.append(i)
                else:
                    if self.precedence(i) > self.precedence(self.atTop()):
                        self.stack.append(i)
                    elif (self.precedence(i) == self.precedence(self.atTop())) and (i == "^"):
                        self.stack.append(i)
                    else:
                        while self.isEmpty() and (self.precedence(i) <= self.precedence(self.atTop())):
                            poped_operator = self.atTop()
                            self.postfix_exp = poped_operator
                            self.delete()



        while not self.isEmpty():
            self.postfix_exp += self.atTop()
            self.delete()









    def delete(self):
        self.stack.pop()



    def display(self):
        print(self.stack)

if __name__ == '__main__':
    s1 = Stack()
    infix_exp = input("Enter infix expression : ")
    s1.insert(infix_exp)
    print(s1.postfix_exp)
