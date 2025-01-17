class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Creating(root):
    print("\tEnter the data")

    data = int(input())
    if data == -1:
        return None
    node = Node(data)
    root = node
    print(f"Enter the data in left of {data}")
    root.left = Creating(root.left)
    print(f"Enter the data in right of {data}")
    root.right = Creating(root.right)
    return root


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


def printing(root):
    if root is None:
        return
    print(root.data)
    printing(root.left)
    printing(root.right)


if __name__ == "__main__":
    root = Node(None)
    root = Creating(root)
    print("printing")
    # printing(root)
    levelOrderTraversal(root)
