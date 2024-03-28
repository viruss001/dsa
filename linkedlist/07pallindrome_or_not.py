from middlell import findmid
from normalll import LinkedList, Node
from reversell import usingrec

head = ll = LinkedList()
# head = ll.creating(2)
head = ll.creating(1)
head = ll.creating(2)
head = ll.creating(3)
head = ll.creating(3)
head = ll.creating(2)
head = ll.creating(1)


class pallindrome:
    def __init__(self, head):
        mid = findmid(head)
        self.head2 = mid.next
        mid.next = None

    def check(self, head1):
        data1 = head1
        data2 = usingrec(self.head2)
        while data1.next and data2.next:
            if data1.data != data2.data:
                return False
            else:
                data1 = data1.next
                data2 = data2.next

        return True


obj = pallindrome(head)
t = obj.check(head)
print(t)
