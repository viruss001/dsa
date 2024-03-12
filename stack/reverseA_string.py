from stack import Stack
stack = Stack()
name="suraj"
ans= ''
for i in range(0,len(name)):
    stack.push(name[i])

while (not(stack.isEmpty())):
    s=stack.pop()
    print(s)
    ans+=s
print(ans)

#print(not stack.isEmpty())

