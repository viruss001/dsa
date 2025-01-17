def kadanealgo(arr):
    maxi,sum=0
    for i in range(0,len(arr)):
        sum+=arr[i]
        maxi=max(maxi,sum)
        if sum<0:
            sum=0
    return maxi