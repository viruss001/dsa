class Stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit
        self.top = -1

    def push(self,data):
        if len(self.stack)>=self.limit:
            return "overflow condition"
        else:
            self.stack.append(data)
            self.top+=1

    def pop(self):
        if len(self.stack)<=0:
            return "underflow condtion"
        else:
            ele = self.stack.pop()
            return ele

    def size (self):
        return len(self.stack)

        
    def isEmpty(self):
        if len(self.stack)<=0:
            return True
        return False