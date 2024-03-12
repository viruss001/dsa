class Node(object):
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        # creating a linkedlist

    def creating(self):
        print("Enter -1 to stop")
        while True:
            print("Enter your data")
            data = int(input())
            newNode = Node(data)
            if data == -1:
                break

            elif self.head == None:
                self.head = newNode
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = newNode
        return self.head

    # printing A linkedlist
    def printing(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("NONE")

    # insert At last
    def insertAtLast(self):
        print("Enter your data")
        data = int(input())
        newNode = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        # insert at head

    def insertAthead(self):
        print("Enter your data")
        data = int(input())
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def afterApostion(self):
        print("enter you choise")
        postion = int(input())
        ptr = self.head
        pre = ptr
        while pre.data != postion:
            pre = ptr
            ptr = ptr.next
        print("Enter your data")
        data = int(input())
        newNode = Node(data)
        newNode.next = ptr
        pre.next = newNode

    def beforeApostion(self):
        print("enter you choise")
        postion = int(input())
        ptr = self.head
        pre = ptr
        while ptr.data != postion:
            pre = ptr
            ptr = ptr.next
        print("Enter your data")
        data = int(input())
        newNode = Node(data)
        newNode.next = ptr
        pre.next = newNode


def printrev(head):
    if head == None:
        return
    else:
        printrev(head.next)
        print(f"{head.data}->", end="")


list = LinkedList()
head_1 = list.creating()
head_2 = list.creating()
