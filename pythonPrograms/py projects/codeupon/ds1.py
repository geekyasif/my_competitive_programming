# creating a node class
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

# creating a linked list class
class linkedList:

    # creating a head or start point of the list contain none at starting when no node is present
    def __init__(self):
        self.head = None

    # creating a method to insert a node when list is empty
    def insert_in_empty_list(self,data):
        new_node = Node(data)
        self.head = new_node


    #inserting node at the begining of the list
    def insert_at_beg(self,data):
        temp = self.head
        new_node = Node(data)
        new_node.next = temp
        self.head = new_node

    # Inserting the node at last of the list or when list is not empty
    def insert_at_last(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # insert before
    def insert_before(self,data,node):
        temp = self.head
        new_node = Node(data)
        while temp.next:
            if temp.next.data == node:
                new_node.next= temp.next
                temp.next = new_node
                return
            temp = temp.next


    # inserting after a node
    def insert_after(self,data,node):
        temp = self.head
        new_node = Node(data)
        while temp:
            if temp.data == node:
                new_node.next = temp.next
                temp.next = new_node
            temp = temp.next

    #deletion of first node or begining
    def del_first_node(self):
        # temp = self.head
        self.head = self.head.next
        return

    # del any node or last node
    def del_in_btw(self,data):
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                prev = temp.next
                temp.next = prev.next
                return
            temp = temp.next

    # deleting the node by its position
    def del_by_pos(self,pos):
        temp = self.head
        count = 0
        while temp:
            if count == pos-1:
                nxt = temp.next
                temp.next = nxt.next
                return
            count +=1
            temp = temp.next
        return


    # Printing the list or traversing the list
    def display_linkedList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print('\n')



if __name__ == '__main__':

    # creating linked list instances or objects to insert in the list
    l1 = linkedList()
    l2 = linkedList()

    # l1.insert_in_empty_list(1)
    # l1.insert_at_last(1)
    # l1.insert_at_last(2)
    # l1.insert_at_last(4)
    # l1.insert_at_last(4)
    # l1.insert_at_last(4)
    # l1.insert_at_last(6)
    # l1.insert_at_beg(0)
    # l1.insert_after(2,0)
    # l1.insert_after(8,6)
    # l1.insert_before(3,5)
    # l1.insert_before(4,6)
    # l1.del_by_pos(6)
    # l1.del_first_node()
    # l1.del_in_btw(0)


    l1.display_linkedList()


