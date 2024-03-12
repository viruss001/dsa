from Tree import Creating, Node


def levelOrderTraversal(root):
    a = []
    a.append(root)
    a.append(None)
    while len(a) != 0:
        temp = a[0]
        a = a[1:]
        if temp is None:
            print("")
            if len(a) != 0:
                a.append(None)
        else:
            print(temp.data, end=" ")
            if temp.left:
                a.append(temp.left)
            if temp.right:
                a.append(temp.right)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.data, end=" ")


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    inorder(root.left)
    inorder(root.right)


root = Node(None)
root = Creating(root)
print("printing")
# printing(root)
# levelOrderTraversal(root)
preorder(root)
print("***")
postorder(root)
print("***")
inorder(root)
