def swapByPosition(arr,a,b):
    if a>len(arr) or b>len(arr):
        print( "index not found in array")
        return None
    else:
        arr[a],arr[b]=arr[b],arr[a]

arr=[1,2,3,5]
swapByPosition(arr,0,2)
print(arr)
