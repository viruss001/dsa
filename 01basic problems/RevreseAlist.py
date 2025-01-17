def reverse(arr):
    aray = [0]*len(arr)
    # create a array size of arr by default size
    # print(aray)
    k=0
    for i in range(len(arr)-1,-1,-1):
         aray[k]=arr[i]
         k+=1
         
    return aray
arr=[1,2,3,5]

print(reverse(arr))
