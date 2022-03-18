class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class circular_linkedList:

    def __init__(self):
        self.head = None

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

    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.head:
                break
        return


    def find_len(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

    def spit_list(self):
        size = self.find_len()
        mid = size//2
        prev = None
        nxt = None
        temp = self.head
        count = 1
        while temp and count < mid:
            temp = temp.next
            count += 1
        nxt = temp.next
        temp.next = self.head
        # printing the first half list
        print("\nfirst half list : ",end= " ")
        self.print_list()

        new_list = circular_linkedList()
        while nxt.next != self.head:
            new_list.insert_node(nxt.data)
            nxt = nxt.next
        new_list.insert_node(nxt.data)
        print('\nsecond half list : ',end=" ")
        new_list.print_list()


if __name__ == '__main__':

    l2 = circular_linkedList()
    l2.insert_node(5)
    l2.insert_node(6)
    l2.insert_node(7)
    l2.insert_node(8)
    l2.insert_node(9)
    l2.insert_node(10)
    print("Full List")
    l2.print_list()
    l2.spit_list()
