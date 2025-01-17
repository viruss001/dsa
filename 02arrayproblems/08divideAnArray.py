def divideArray(arr):
    totoalsum=0
    for i in range(len(arr)):
        totoalsum+=arr[i]
    prefix=0
    for i in range(len(arr)):
        prefix+=arr[i]
        ans=totoalsum-prefix 
        if ans==prefix:
            return 1
    return 0
print(divideArray([3,4,-2,5,8,20,-10,8]))