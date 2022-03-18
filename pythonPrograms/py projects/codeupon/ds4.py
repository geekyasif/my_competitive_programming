# program to swap node in singly linked list
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

    # swapping two node
    def swap_node(self,node1,node2):
        prev1 = None
        cur1 = None
        prev2 = None
        cur2 = None
        temp = self.head

        while temp.next:
            if temp.next.data == node1:
                prev1 = temp
                cur1 = temp.next
            elif temp.next.data == node2:
                prev2 = temp
                cur2 = temp.next
            temp = temp.next

        prev1.next = cur2
        nxt3 = cur2.next
        cur2.next = prev2
        cur1.next = nxt3
        return



if __name__ == '__main__':
    l1 = Linkedlist()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(4)
    l1.push(5)
    l1.push(6)
    l1.push(7)
    l1.printlist()
    print('')
    l1.swap_node(5,6)
    l1.printlist()
