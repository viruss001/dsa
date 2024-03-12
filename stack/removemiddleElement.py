from stack import Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
#stack.push(5)
stack1 = Stack()
size = stack.size()//2
count = 0



while not count is size:
    
    stack1.push(stack.pop())
    count+=1
stack.pop()
while not stack1.isEmpty():
    stack.push(stack1.pop())

while (not(stack.isEmpty())):
    s=stack.pop()
    print(s)
