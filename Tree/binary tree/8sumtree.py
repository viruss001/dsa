from Tree import Creating, Node
root = Node(None)
root=Creating(root)
def sum(root):
    if root is None:
        return [True,0]
    if root.left is None and root.right is None:
        return [True,root.data]
    leftans=sum(root.left)
    rightans=sum(root.right)
    left=leftans[0]
    right=rightans[0]
    ans=[]
    if left and right:

        condi=root.data==leftans[1]+rightans[1]
        if right and left and condi:
            ans.append(True)
            ans.append(root.data+leftans[1]+rightans[1])
        else:
            ans.append(False)
    else:
        ans.append(False)
    return ans
print(sum(root))