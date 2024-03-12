from normalll import head_2
temp = head_2
while(temp is not None and temp is not head_2):
    temp= temp.next
if(temp is None):
    print("True")
if(temp is head_2):
    print("False")