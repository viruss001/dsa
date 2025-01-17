from dummytree import root
def solution(root,k,node):
    if root is None:return None
    if root.data==node:
        return root
    left=solution(root.left,k,node)
    right=solution(root.right,k,node)
    if left is not None and right is None:
        k-=1
        if k<=0:
            k=100
            return root
        return left
    if left is None and right is not None:
        k-=1
        if k<=0:
            k=100
            return root
        return right
    return None
a=solution(root,3,1)
print(a.data)