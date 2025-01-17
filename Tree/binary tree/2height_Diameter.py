from Tree import Creating, Node

root = Node(None)
root = Creating(root)

def height(root):
    if root is None:
        return 0
    else:
        count1 = height(root.left)

        count2 = height(root.right)

        anm = max(count1, count2) + 1
        print(anm)
        return anm
def diameter(root):
    if root is None:
        return [0,0]
    left=diameter(root.left)
    right=diameter(root.right)
    opt1=left[0]
    opt2=right[0]
    opt3=left[1]+right[1]+1
    ans=[0,0]
    ans[0]=max(opt1,max(opt2,opt3))
    ans[1]=max(left[1],right[1]+1)
    return ans


count = height(root)
print(count)
