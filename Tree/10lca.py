from Tree import Creating, Node
root = Node(None)
root=Creating(root)
def lca(root,n1,n2):
    if root is None:
        return None
    if root.data is n1 or root.data is n2:
        return root
    left= lca(root.left,n1,n2)
    right= lca(root.right,n1,n2)
    if left is not None and right is  None:
        return left
    elif left is  None and right is not None:
        return right
    elif left is not None and right is not None:
        return root
    else:
        return None
a=lca(root,4,21)
print(a.data)