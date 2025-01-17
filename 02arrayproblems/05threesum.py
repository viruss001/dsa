def TwoSumUnsortedArray(i,arr,target):
    dic={}
    print(arr)
    if i<len(arr)+i-1:

        for j in range(i,len(arr)):
            ans=target-arr[j]
            if ans in dic:
                return([dic[ans],i+j])
            else:
                dic[arr[i]]=i+j
                print(dic)
    return None

def threesum(arr,target):
    ans=None
    for i in range(len(arr)):
        new_target=target-arr[i]
        print(new_target)
       
        ans=TwoSumUnsortedArray(i+1,arr,target=new_target)
        if ans is not None:
            break
    if ans is None:
        print("sorry")
    else:
        print(ans,i)

threesum([1,4,45,6,10,8],11)