from normalll import LinkedList, Node


# from normalll import head_2
def findmid(head):
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = ll = LinkedList()
    # head = ll.creating(2)
    head = ll.creating(1)
    head = ll.creating(2)
    head = ll.creating(36)
    head = ll.creating(3)
    head = ll.creating(4)
    head = ll.creating(5)
    ll.printing()
    mid = findmid(head)
    print(mid.data)
