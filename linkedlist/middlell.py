from normalll import head_2
def findmid(head):
    slow = head
    fast = head.next
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow
if __name__=="__main__":
    print(findmid(head_2).data)