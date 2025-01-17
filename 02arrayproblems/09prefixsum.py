def prefixsum(arr):
    prefix=0
    for i in range(len(arr)):
        prefix+=arr[i]
        arr[i]=prefix