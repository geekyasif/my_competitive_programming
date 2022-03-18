class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = Node(data)
        temp = self.head
        if (self.head is None) or (new_node.data < temp.data):
            self.head = new_node
            new_node.next = temp
            return
        else:
            while (temp.next != None) and (temp.next.data < new_node.data):
                temp = temp.next
            nxt = temp.next
            temp.next = new_node
            new_node.next = nxt
            return

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    l1 = Linkedlist()
    l1.insert_node(5)
    l1.insert_node(2)
    l1.insert_node(1)
    l1.insert_node(0)
    l1.insert_node(8)
    l1.insert_node(7)
    l1.insert_node(6)
    l1.insert_node(4)
    l1.insert_node(3)
    l1.insert_node(9)
    l1.insert_node(10)
    l1.insert_node(55)
    l1.insert_node(23)
    l1.insert_node(45)
    l1.print_list()