from dummytree import root

def solution(rot,k,node):
    if rot is None:
        return None
    if rot.data is node:
        return rot
    leftans=solution(rot.left,k,node)
    rightans=solution(rot.right,k,node)
    if leftans is not None and rightans is None:
        k-=1
        if k<=0:
            k=100
            return rot
        return leftans
    if leftans is None and rightans is not None:
        k-=1
        if k<=0:
            k=100
            return rot
        return rightans
    return None

def kthancestor():
    ans=solution(root,1,2)
    print(ans.data)


kthancestor()
