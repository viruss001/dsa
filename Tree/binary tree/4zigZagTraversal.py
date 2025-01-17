from Tree import Creating, Node
def zigZag(root):
    result=[]
    if root is None:
        return result
    q = []
    q.append(root)
    leftToRight=True
    while (len(q)!=0):
        size = len(q)
        ans=[0]*size
        for i in range(0,size):
            frontnode=q[0]
            q=q[1:]
            index=0
            if leftToRight:
                index=i
            else:
                index = size-i-1
            ans[index]=frontnode.data
            if frontnode.left:
                q.append(frontnode.left)
            if frontnode.right:
                q.append(frontnode.right)
        leftToRight = not leftToRight
        for i in ans:
            result.append(i)
    return result
root = Node(None)
root=Creating(root)
a=zigZag(root=root)
print(a)