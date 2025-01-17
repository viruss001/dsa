from Tree import Creating, Node
def Balance(root):
    if root is None:
        return [True,0]
    left=Balance(root.left)
    right=Balance(root.right)
    #geting first value 
    leftans=left[0]
    rightans=right[0]
    #accorging to condtion
    dif=abs(left[1]-right[1])<=1
    ans=[0,0]
    #height of tree
    ans[1]=max(left[1],right[1])+1
    if leftans and rightans and dif:
        ans[0]=True
    else:
        ans[0]=False
    return ans
root = Node(None)
root=Creating(root)
a= Balance(root)
print(a[0])