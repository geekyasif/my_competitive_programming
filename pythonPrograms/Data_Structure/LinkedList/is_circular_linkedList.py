class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class single_linkedList:

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
            print(temp.data, end=" ")
            temp = temp.next
        return

class circular_linkedList:

    def __init__(self):
        self.head = None

    # inserting the node
    def insert_node(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            return


    # printing the list
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.head:
                break

        return

    # cheacking the list is circular or not
    def is_cirular(self,list):
        p = list.head
        while p.next:
            if p.next == self.head:
                print("\ntrue")
                return
            p = p.next
        print("\nfalse")


if __name__ == '__main__':
    l1 = single_linkedList()
    l1.insert_node(1)
    l1.insert_node(2)
    l1.insert_node(3)
    l1.insert_node(4)
    l1.print_list()
    print('')
    l2 = circular_linkedList()
    l2.insert_node(5)
    l2.insert_node(6)
    l2.insert_node(7)
    l2.insert_node(8)

    l2.print_list()
    # l2.is_cirular(l2)
    print('')
    print(l2.find_len())

