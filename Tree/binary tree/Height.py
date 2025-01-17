from Tree import Creating, Node

root = Node(None)
root = Creating(root)


def height(root, count):
    if root is None:
        return count
    else:
        count += 1
        print(count)
        count1 = height(root.left, count)
        print(count1, " iam cont 1")
        count2 = height(root.right, count)
        print(count2, "i am count 2")
        if count1 >= count2:
            return count1
        else:
            return count2


def height1(root):
    if root is None:
        return 0
    else:
        count1 = height1(root.left)

        count2 = height1(root.right)

        anm = max(count1, count2) + 1
        print(anm)
        return anm


def deameater(root):
    if root is None:
        return 0
    opt1 = deameater(root.left)
    opt2 = deameater(root.right)
    opt3 = height1(root.left) + height1(root.right) + 1
    anm = max(opt3, max(opt1, opt2))
    return anm


count = height1(root)
print(count)
