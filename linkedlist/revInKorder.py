from normalll import head_2
def kReverse(head,k):
    if(head == None) :
        return None
    next = None
    curr = head
    prev = None
    count= 0
    while(curr is not None and count<k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count+=1
    if(next != None) :
        head . next = kReverse(next,k)
    
    return prev
def printing(head):
    if(head == None):
        return
    else:
        print(f"{head.data}->",end="")
        printing(head.next)
    

head_3=kReverse(head_2,2)
printing(head_3)