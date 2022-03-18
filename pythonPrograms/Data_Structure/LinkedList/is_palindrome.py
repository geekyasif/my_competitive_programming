class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            return

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        return

    def is_palindrome_string(self):
        ''' this method is use to cheack string value'''
        s = ""
        temp = self.head
        while temp:
            s += temp.data
            temp = temp.next

        if s == s[::-1]:
            print("\nTrue")
        else:
            print("\nFalse")


    def is_palindrome_stack(self):
        ''' This method is to check integer value'''
        s = []
        temp = self.head
        while temp:
            s.append(temp.data)
            temp = temp.next
        temp = self.head
        while temp:
            data = s.pop()
            if temp.data != data:
                print("\nFalse")
                return
            temp = temp.next
        print("\nTrue")

    def is_palindrome_two_pointer(self):
        pass

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_node(1)
    l1.insert_node(2)
    l1.insert_node(1)
    l1.print_list()
    l1.is_palindrome_stack()

