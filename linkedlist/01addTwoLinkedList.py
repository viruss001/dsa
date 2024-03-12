from normalll import LinkedList
list1 = LinkedList()
head = list1.creating(5) 
head = list1.creating(6) 
head = list1.creating(4) 
list2 = LinkedList()
head = list2.creating(2) 
head = list2.creating(4) 
head = list2.creating(3) 
#list1.printing()
#list2.printing()
temp1 = list1.head
temp2 = list2.head
n1 = 0
n2 = 0
while(temp1 is not None or temp2 is not None):
    n1,n2 = n1*10,n2*10
    n1=n1+temp1.data
    n2=n2+temp2.data
    temp1,temp2 = temp1.next,temp2.next
#print(n1)
#print(n2)
def rev(n):
    sum = 0
    
    while n != 0:
        rev = n%10 
        sum =sum*10+rev
        n = n//10
    return sum    

rev1 = rev(n1)
rev2 = rev(n2)
print(rev1)
print(rev2)
print(rev1+rev2)