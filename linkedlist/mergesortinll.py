from middlell import findmid
from normalll import head_2 as head


# we have to change only links not data
class Node(object):
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    ans = Node(-1)
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


def mergesort(head):
    # base condition
    if head is None or head.next is None:
        return head
    # breaking the list in two parts after findindmid
    mid = findmid(head)
    left = head  # contain 1 part
    right = mid.next  # contain 2 part
    mid.next = None
    # recursion call
    left = mergesort(left)
    right = mergesort(right)
    # merging both list
    result = merge(left, right)
    return result


def printing(head):
    if head is None:
        return
    else:
        print(f"{head.data}", end="->")
        printing(head.next)


# mergesort(head)
# printing(head)
printing(mergesort(head))
