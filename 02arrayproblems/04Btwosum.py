# work on unsorted array
def TwoSumUnsortedArray(arr,target):
    dic={}
    for i in range(len(arr)):
        ans=target-arr[i]
        if ans in dic:
            return([dic[ans],i])
        else:
            dic[arr[i]]=i
    
a=TwoSumUnsortedArray([1,4,45,6,10,8],5)
print(a)