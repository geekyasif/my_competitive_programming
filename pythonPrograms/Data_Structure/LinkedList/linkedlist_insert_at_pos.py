#program to find the position of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head
        new_data = Node(data)
        if temp is None :
            self.head = new_data
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_data

    def find_pos(self):
        temp = self.head
        pos = int(input("Enter the position: "))

        count = 1
        # if pos == 1:
        #     print(temp.data)
        # else:
        #     while count != pos:
        #         temp = temp.next
        #         count += 1
        #
        # print(temp.data)

        if pos ==1:
            print(temp.data)
        else:
            while temp:
                temp = temp.next
                count += 1
                if pos == count:
                    print(temp.data)
                    break





    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(5)
    l1.insert(232)
    l1.insert(4231)
    l1.insert(422332331)
    l1.insert(231)
    l1.display()
    l1.find_pos()

