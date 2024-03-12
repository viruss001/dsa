class Node(object):
    def __init__(self ,data,next = None):

        self.data = data 
        self.next = next
class Linkedlist(object):
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def create(self,data):
        newode = Node(data)
        if self.head ==None:
            self.head = newode
            self.tail =newode
            self.head.next = self.tail
            self.tail.next = self.head
        else:
            newode.next=self.head
            self.tail.next= newode
            self.tail = newode
    

    def insertAtstart(self,data):
            newode = Node(data)
            newode.next= self.head
            self.head = newode
            self.tail.next=self.head
            
    def insertAtlast(self,data):
            newode = Node(data)
            newode.next=self.head
            self.tail.next  = newode
            self.tail = newode
        
    def printing(self):
        temp = self.head
        while(temp.next!=self.head):
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(f"{temp.data}->",end="")
        print("Head")
link = Linkedlist()
link.create(5)
link.create(5)
link.create(5)
link.create(5)
link.create(5)
link.create(5)
link.insertAtstart(7)
link.printing()
