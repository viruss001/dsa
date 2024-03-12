from normalll import LinkedList


def uniqueSortedList(head):
    if head == None:
        return None

    curr = head

    while curr != None:
        if (curr.next != None) and curr.data == curr.next.data:
            curr.next = curr.next.next

        else:
            curr = curr.next

    return head


def printing(head):
    if head == None:
        return
    else:
        print(f"{head.data}", end="->")
        printing(head.next)
    # print("none")


head = ll = LinkedList()
head = ll.creating(1)
head = ll.creating(2)
head = ll.creating(2)
head = ll.creating(3)
head = ll.creating(3)
head = ll.creating(5)
head = ll.creating(4)
printing(head)
print("")
printing(uniqueSortedList(head))
