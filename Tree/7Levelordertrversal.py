from Tree import Creating, Node
root = Node(None)
root=Creating(root)
def levelorder(root):
    a=[root]
    a.append(None)
    while(len(a)!=0):
        temp=a[0]
        a=a[1:]
        if temp is None:
            print(" ")
            # at this point we traver a perticular order
            if(len(a)!=0):
                a.append(None)
        else:
            print(temp.data ,end=" ")
            if temp.left:
                a.append(temp.left)
            if temp.right:
                a.append(temp.right)

levelorder(root)