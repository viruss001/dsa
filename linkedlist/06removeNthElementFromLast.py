from normalll import LinkedList
l = LinkedList()
head = l.creating(1)
head = l.creating(2)
head = l.creating(3)
head = l.creating(4)
head = l.creating(5)
head = l.creating(6)
#l.printing()
#declear the last value
temp = head.next
last = 0
while(temp is not None):
    last+=1
    temp = temp.next
#print(last)
pre= head.next
value= 0
current = head
while(last-value!=2):
 current =pre
 pre=pre.next
 value+=1
print(pre.data)
current.next = pre.next
l.printing()

