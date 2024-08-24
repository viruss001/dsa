from Tree import Creating, Node
root = Node(None)
root=Creating(root)
def solution(root,sum,len,maxi):
    if root is None:
        if len>maxi[1]:
                maxi[0]=sum
                maxi[1]=len