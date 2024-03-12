from normalll import LinkedList


class List:
    def __init__(self):
        self.ll = LinkedList()

    def creat(self):
        bool = True
        print("Enter the element\n-11for exit")
        while bool:
            n = int(input())
            if n == -11:
                return self.ll
            else:
                self.ll.creating(n)
        return self.ll.head

    def printing(self):
        self.ll.printing()
