from Tree import Creating, Node
def no_leaf_node(root,count):
    #base case 
    if root is None:
        return 
    if root.left is None and root.right is None: 
        count[0]+=1
    no_leaf_node(root.left,count)
    no_leaf_node(root.right,count)
root = Node(None)
root=Creating(root)
count=[0]#we send as refernce variable
no_leaf_node(root,count)
print(count[0])