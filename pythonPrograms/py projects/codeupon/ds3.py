# Program to find the length of singly linked list

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    # inserting the node to the list
    def push(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            temp = self.head
            new_node = Node(data)
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # printing the linked list or traversing the list
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    # finding the lenght of the singly linked list
    def find_len(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print('')
        print(count)



if __name__ == '__main__':
    l1 = Linkedlist()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(4)
    l1.printlist()
    l1.find_len()


