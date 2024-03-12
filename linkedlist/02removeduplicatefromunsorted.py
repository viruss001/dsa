from normalll import LinkedList

head = ll = LinkedList()
head = ll.creating(1)
head = ll.creating(2)
head = ll.creating(2)
head = ll.creating(3)
head = ll.creating(3)
head = ll.creating(5)
head = ll.creating(4)


def uniqueSortedList(head):
    if head is None:
        return None

    curr = head
    # check = head
    while curr is not None and curr.next is not None:
        check = curr
        while check is not None and check.next is not None:
            if curr.data is check.next.data:
                print(f"{curr.data} is curr and {check.next.data} is check.next.data")
                check.next = check.next.next
            check = check.next
        curr = curr.next
    return head


def printing(head):
    if head is None:
        return
    else:
        print(f"{head.data}", end="->")
        printing(head.next)


printing(uniqueSortedList(head))
