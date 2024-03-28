from normalll import LinkedList, Node

head = ll = LinkedList()
head = ll.creating(1)
head = ll.creating(2)
head = ll.creating(2)
head = ll.creating(3)
head = ll.creating(3)
head = ll.creating(4)
head = ll.creating(5)


class RemoveDulicate:
    def __init__(self):
        self.fake = Node(-1)

    def function(self, head):
        self.fake.next = head
        curr = head
        pre = self.fake
        while curr:
            while curr.next and curr.next.data == curr.data:
                curr = curr.next
            if pre.next == curr:
                pre = pre.next
                curr = curr.next

            else:
                pre.next = curr.next
                curr = pre.next
        temp = head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("NONE")


obj = RemoveDulicate()


obj.function(head)


# def printing(head):
#     temp = head
#     while temp:
#         print(f"{temp.data}->", end="")
#         temp = temp.next
#     print("NONE")
