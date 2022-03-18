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

    def insert_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


    # insert before
    def insert_before(self,data,node):
        temp = self.head
        new_node = Node(data)
        while temp:
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


    # reversing a linked list
    def reverse_list(self):
        prev = None
        nxt = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        return


    #deletion of first node or begining
    def del_first_node(self):
        # temp = self.head
        self.head = self.head.next
        return


    # del any node or last node
    def del_in_btw(self,data):
        temp = self.head
        while temp:
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


    #swappping two nodes
    def swaping_node(self,nodeA,nodeB):
        temp = self.head
        prev1 = None
        current1 = None
        prev2 = None
        current2 = None
        while temp.next:
            if temp.next.data == nodeA:
                prev1 = temp
                current1 = temp.next
            elif temp.next.data == nodeB:
                prev2 = temp
                current2 = temp.next
            temp = temp.next

        prev1.next = current2
        current2_nxt = current2.next
        current2.next = current1
        current1.next = current2_nxt.next
        return


    #nth node of linked list
    def nth_node(self):
        temp = self.head
        prev = None
        while temp.next:
            prev = temp.data
            temp = temp.next
        print(prev)
        return


    #count the length of the linked list
    def find_len(self):
        temp = self.head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        print(f"Lenght of the linked list is {len}")
        return


    # find the occurance of the list
    def find_node_occr(self,node):
        temp = self.head
        count = 0
        while temp:
            if temp.data == node:
                count += 1
            temp = temp.next
        print(f"{node} is found {count} times")
        return


    # swapping head and tail of a list
    def move_tail_to_head(self):
        temp = self.head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next = self.head
        self.head = temp
        return


    # rotating a list from a given node position
    def rotate(self,node):
        temp = self.head
        rotate = None
        new_head = None
        while temp.next:
            if temp.data == node:
                rotate = temp
                new_head = temp.next
            temp = temp.next
        last_node = temp
        last_node.next = self.head
        self.head = new_head
        rotate.next = None
        return self.head


    # pairswapping of a singly linked list
    def pair_swap(self):

        temp = self.head
        # if temp is None:
        #     return
        while temp:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        return
    # if temp.data == temp.next.data:
    #             temp = temp.next.next
    #         else:


    # adding each node of singly linked list
    def sum_two_list(self,l1,l2):
        prev = None
        temp = None
        carry = 0
        while l1 is not None or l2 is not None:

            # cheacking l1 or l2 none or not
            if l1 is None:
                l1_data = 0
            else:
                l1_data = l1.data
            if l2 is None:
                l2_data = 0
            else:
                l2_data = l2.data

            # adding each data from linkedlist
            sum = carry + l1_data + l2_data

            #updating carry
            if sum >= 10:
                carry = 1
            else:
                carry = 0

            #updating sum
            if sum < 10:
                sum = sum
            else:
                sum = sum%10

            #creating a new node of sum
            temp = Node(sum)

            #and inserting into a new list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            #set prev for next insertion
            prev = temp

            # moving the node to the next node
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if carry > 0:
                temp.next = Node(carry)


    #remove duplicates in sorted linked list
    # remove duplicate in a linked list if next is same else it will not work
    def remove_duplicate(self):
        temp = self.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                nxt = temp.next.next
                temp.next = None
                temp.next = nxt
            else:
                temp = temp.next
        return

    #unsorted removal of duplicate nodes not working properly
    def remov_dup(self):
        cur = self.head
        prev = None
        dup_vals = dict()
        while cur:
            if cur.data in dup_vals:
                prev.next = cur.next
                cur = None
            else:
                dup_vals[cur.data] = 1
                prev = cur
                cur = cur.next
        return

    # remove duplicates working properly
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

    # Printing the list or traversing the list
    def display_linkedList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print('\n')

    #mergin two sorted linked list
    def merge(self,l2):
        p = l1.head
        q = l2.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not q:
            s.next = p
        if not p:
            s.next = q

        return new_head


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

    # creating linked list instances or objects to insert in the list
    l1 = linkedList()
    l2 = linkedList()
    l3 = linkedList()

    # l1.insert_in_empty_list(1)
    # l1.insert_at_last(1)
    l1.insert_at_beg(1)
    l1.insert_at_last(5)
    l1.insert_at_last(6)
    l1.insert_at_last(8)
    # l1.remove_duplicate()
    # l1.display_linkedList()
    # l1.remove_duplicate()



    # l3 = linkedList()
    # l3.sum_two_list(l1.head,l2.head)

    # l1.insert_at_beg(0)
    # l1.insert_after(2,0)
    # l1.insert_after(8,6)
    # l1.insert_before(3,5)
    # l1.insert_before(4,6)
    # l1.reverse_list()
    # l1.del_by_pos(6)
    # l1.del_first_node()
    # l1.del_in_btw(0)
    # l1.swaping_node(8,6)
    # l1.nth_node()
    # l1.find_len()
    # l1.find_node_occr(3)
    # l1.rotate(5)

    # l1.pair_swap()

    # l1.display_linkedList()
    # l2.display_linkedList()
    # l3.display_linkedList()

    l2.insert_at_beg(2)
    l2.insert_at_last(3)
    l2.insert_at_last(4)
    l2.insert_at_last(7)
    l2.display_linkedList()
    l2.is_circular()

    # l1.merge(l2)
    # l1.display_linkedList()

