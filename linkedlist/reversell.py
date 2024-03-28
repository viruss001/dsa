# linked list
# from normalll import head_2
# print(head_2)
# funtion using loop
from normalll import LinkedList, Node


def usingrec(head):
    if head is None or head.next is None:
        return head
    chotahead = usingrec(head.next)
    head.next.next = head
    head.next = None
    return chotahead


# priting list
def printing(head):
    if head == None:
        return
    else:
        print(f"{head.data}->", end="")
        printing(head.next)


def usingloop(head):
    next = None
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


if __name__ == "__main__":
    head = ll = LinkedList()
    # head = ll.creating(2)
    head = ll.creating(1)
    head = ll.creating(2)
    head = ll.creating(3)
    head = ll.creating(3)
    head = ll.creating(2)
    head = ll.creating(1)
