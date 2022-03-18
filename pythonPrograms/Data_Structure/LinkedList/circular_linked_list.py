class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    # insert at beg if node is empty or not
    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            new_node.next = temp
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    # insert when list is empty or at the end
    def insert_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head


    # insert before
    def insert_before(self,data,node):
        temp = self.head
        if temp.data == node:
            self.insert_at_beg(data)
        else:
            new_node = Node(data)
            while temp.next != self.head:
                if temp.next.data == node:
                    new_node.next = temp.next
                    temp.next = new_node
                    return
                temp = temp.next

    # insert after a node
    def insert_after(self,data,node):
        new_node = Node(data)
        temp = self.head
        while temp.next != self.head:
            if temp.data == node:
                nxt = temp.next
                temp.next = new_node
                new_node.next = nxt
            temp = temp.next
        return

    #del first node
    def del_first(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        return

    #deleting last node
    def del_last(self):
        if self.head is None:
            print('list is empty')
        else:
            temp = self.head
            prev = None
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = temp.next
        return


    #finding the length of the circular liked list
    def len(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            if temp.next is self.head:
                break
            temp = temp.next
        return count



    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.head:
                break

    # cheacking linked list is circular or not
    def is_circular(self):
        temp = self.head
        while temp.next:
            temp = temp.next
            if temp.next == self.head:
                print("true")
                return
        print("false")



if __name__ == '__main__':
    l1 = CircularLinkedList()
    l1.insert_node(1)
    l1.insert_node(2)
    l1.insert_node(3)
    l1.insert_at_beg(4)
    l1.insert_node(5)
    l1.insert_before(0,4)
    l1.insert_before(6,5)
    l1.insert_after(9,3)
    l1.del_first()
    l1.del_last()
    print(l1.len())
    l1.printlist()
    l1.is_circular()
