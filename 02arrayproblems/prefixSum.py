arr=[6,4,5,-3,2,8]
prefixsum=[0]*len(arr)
# print(arr,prefixsum)
sum=0
for i in range(0,len(arr)):
    sum+=arr[i]
    arr[i]=sum
print(arr,prefixsum)

