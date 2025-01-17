def swap(arr):
    arr[0],arr[len(arr)-1]=arr[len(arr)-1],arr[0]


arr=[1,2,3,5]
swap(arr)
#pass by reffrence 
# if wants to send a copy of an array then 
swap(arr[:])
print(arr)