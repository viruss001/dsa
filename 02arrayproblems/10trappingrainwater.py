# with extra space
def extraspace(arr):
    maxleft=[0]*len(arr)-1
    maxright=[0]*len(arr)-1
    maxleft[0]=0
    for i in range(1,len(arr)):
        maxleft[i]=max(maxleft[i-1],arr[i-1])
    maxright[len(arr)-1]=0
    for i in range(len(arr)-2,-1,-1):
        maxright[i]=max(maxright[i+1],arr[i+1])
    waterstore=0
    for i in range(0,len(arr)):
        mini=min(maxleft[i],maxright[i])
        if mini-arr[i]>=0:
            waterstore+=mini-arr[i]
    return waterstore
