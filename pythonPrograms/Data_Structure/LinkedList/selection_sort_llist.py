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
        if self.head is None:
            self.head = new_node
            return
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            return

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    def sort_by_data(self):
        p = self.head
        while p:
            q = p.next
            while q:
                if p.data > q.data:
                    first_data = p.data
                    second_data = q.data
                    q.data = first_data
                    p.data = second_data
                q = q.next
            p = p.next
        return

    # def sort_by_link(self):
    #     p = self.head
    #     while p:
    #         q = p.next
    #         while q:
    #             if p.data > q.data:
    #                 prev1 = p
    #                 next1 = p.next
    #                 prev2 = q
    #                 next2 = q.next
    #



if __name__ == '__main__':
    l1 = Linkedlist()
    l1.insert_node(4)
    l1.insert_node(2)
    l1.insert_node(5)
    l1.insert_node(1)
    l1.insert_node(3)
    l1.print_list()
    print(' ')
    l1.sort_by_data()
    l1.print_list()
