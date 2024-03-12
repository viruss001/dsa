class Node(object):
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        # creating a linkedlist

    def creating(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        return self.head

    def printing(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("NONE")
