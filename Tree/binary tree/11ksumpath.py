from dummytree import root
def solution(root,k,count,path):
    if root is None:
        return
    path.append(root.data)
    solution(root.left,k,count,path)
    solution(root.right,k,count,path)
    sum=0
    # print(len(path)-1)
    # print(path)
    for i in range(len(path)-1,-1,-1):
        
        sum+=path[i]
        if sum==k:
            # print(count[0])
            count[0]+=1
    path.pop()

path=[]
count=[0]
solution(root,5,count,path)
print(count[0])