from normalll import LinkedList

# first linked list
list1 = LinkedList()
head1 = list1.creating(1)
head1 = list1.creating(3)
head1 = list1.creating(4)
# second linked list
list2 = LinkedList()
head2 = list2.creating(2)
head2 = list2.creating(3)
head2 = list2.creating(4)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    ans = LinkedList()
    ans.creating(-1)
    temp = ans
    while left is not None and right is not None:
        if left.data >= right.data:
            temp.next = right
            temp = right
            right = right.next
        else:
            temp.next = left
            temp = left
            left = left.next
    while left is not None:
        temp.next = left
        temp = left
        left = left.next
    while right is not None:
        temp.next = right
        temp = right
        right = right.next
    return ans.next


l = merge(head1, head2)


def printing(l):
    temp = l
    while temp:
        print(f"{temp.data}->", end="")
        temp = temp.next
    print("NONE")


printing(l)
