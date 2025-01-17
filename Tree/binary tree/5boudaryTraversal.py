from Tree import Creating, Node
root = Node(None)
root=Creating(root)
def left(root,arr):
    if root is None or root.left is None and root.right is None:
        return
    arr.append(root.data)
    if root.left:
        left(root.left,arr)
    else:
        left(root.right,arr)

def right(root,arr):
    if root is None or root.left is None and root.right is None:
        return
    
    if root.right:
        right(root.right,arr)
    else:
        right(root.left,arr)
    arr.append(root.data)
def leaf(root,arr):
    if root is None:
        return
    if root.left is None and root.right is None:
        arr.append(root.data)
        return
    leaf(root.left,arr)
    leaf(root.right,arr)


def BoundryTraversal(root):
    if root is None:
        return None
    arr=[root.data]
    left(root.left,arr)
    leaf(root,arr)
    right(root.right,arr)
    return arr
a=BoundryTraversal(root)
print(a
      )