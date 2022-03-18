class Node:

    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class doublyLinkedList:

    def __init__(self):
        self.head = None

    # inserting at the begining
    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

    #inserting at the end
    def insert_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return

    def insert_after_a_node(self,data,node):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.data == node:
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                return
            temp = temp.next


    def insert_before(self,data,node):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.next.data == node:
                temp.next.prev = new_node
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                return
            temp = temp.next

    # deleting the first node
    def del_at_beg(self):
        self.head = self.head.next
        self.head.next.prev = None

    # deleteing the last node
    def del_at_last(self):
        temp = self.head
        while temp:
            if temp.next is None:
                prev = temp.prev
                prev.next = None
                return
            temp = temp.next

    # deleting any node betweeen first and last
    def del_in_btw(self,node):
        temp = self.head
        while temp:
            if temp.next.data == node:
                nxt = temp.next
                temp.next = nxt.next
                temp.next.prev = temp
                return
            temp = temp.next


    #reversing a linked list
    def reverse_dlist(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        self.head = temp.prev



    # traversing the linked list
    def displayList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


    #pair of sum
    def pair_sum(self,sum_val):
        p = self.head
        lst = []
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    lst.append(f"({p.data},{q.data})")
                q = q.next
            p = p.next

        if len(lst) == 0:
            print("\nNo pair of sum is found")
        else:
            print(f'\n{lst}')


    # remove duplicates
    def remove_duplicate(self):
        p = self.head
        while p:
            q = p.next
            while q:
                if p.data == q.data:
                    self.del_in_btw(q.data)
                q = q.next
            p = p.next
        return


if __name__ == '__main__':
    l1 = doublyLinkedList()
    l1.insert_at_beg(1)
    l1.insert_at_beg(2)
    l1.insert_at_beg(2)
    l1.insert_at_beg(2)
    l1.insert_at_beg(2)
    l1.insert_at_beg(2)
    l1.insert_at_end(3)
    l1.insert_after_a_node(4,3)
    l1.insert_before(2,3)
    l1.insert_before(5,4)
    l1.insert_before(4,3)
    l1.insert_before(2,5)
    l1.insert_before(3,1)
    # l1.del_at_beg()
    # l1.del_in_btw(1)
    # l1.del_at_last()

    # l1.displayList()
    # print('\n')
    # l1.reverse_dlist()
    l1.displayList()
    l1.remove_duplicate()
    print('\n')
    l1.displayList()
    # l1.pair_sum(4)


