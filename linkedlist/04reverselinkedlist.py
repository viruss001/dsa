from normalll import LinkedList


class Reverse:
    def __init__(self):
        pass

    def reverse(self, head, left, right):
        # setting left
        count = 1
        left_node = None
        pre_left_node = None
        temp = head
        while count is not left:
            pre_left_node = temp
            temp = temp.next
            count += 1
        left_node = temp
        # setting right
        count = 1
        right_node = None
        post_right_node = None
        temp = head

        while count is not right:
            count += 1
            temp = temp.next
        right_node = temp
        post_right_node = right_node.next
        right_node.next = None
        # print(left_node.next)
        chota_head = self.reverseLinkedList(left_node)
        pre_left_node.next = chota_head
        left_node.next = post_right_node

    def reverseLinkedList(self, head):
        if head is None or head.next is None:
            return head
        chota_head = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None
        return chota_head


ll = LinkedList()
head = ll.creating(1)
head = ll.creating(2)
head = ll.creating(4)
head = ll.creating(6)
head = ll.creating(3)
head = ll.creating(5)
head = ll.creating(7)
head = ll.creating(8)
obj = Reverse()
obj.reverse(head, 3, 6)
ll.printing()
