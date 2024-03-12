class Node(object):
    def __init__(self,data,prev= None,next=None) -> None:
        self.prev = prev
        self.data =  data
        self.next = next
class Double(object):
    def __init__(self) -> None:
        self.head = None
        self.tail=None
    def creating(self):
        
        print("Enter -1 to stop")
        while(True):
            print("Enter your data")
            data = int(input())
            newNode =Node(data)
            if(data ==-1):
                
                break
            
            elif(self.head ==None):
                self.head =newNode
                self.tail = newNode
            else:
                temp = self.head
                while(temp.next!=None):
                    temp = temp.next
                temp.next =newNode
                newNode.prev = temp
                self.tail = newNode
                
        return self.head
    def printing(self):
        temp = self.head
        
        while(temp):
            print(f"{temp.data}->",end="")
            temp = temp.next
        print("NONE")
        temp1 = self.tail
        while(temp1):
            print(f"{temp1.data}->",end="")
            temp1 = temp1.prev
        print("NONE")
    def insertAtlast(self):
        print("Enter your data")
        data = int(input())
        newNode =Node(data)
        self.tail.next=newNode
        newNode.prev=self.tail
        self.tail = newNode

        
link = Double()
link.creating()
link.printing()
link.insertAtlast()
link.printing()