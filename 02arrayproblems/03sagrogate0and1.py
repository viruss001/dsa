def segregate0and1(arr):
    count0=0
    count1=0
    for i in range(0,len(arr)):
        if arr[i]==0:
            count0+=1
        else:
            count1+=1

   
    for i in range(0,count0):
        arr[i]=0
    for i in range(count0,len(arr)):
        arr[i]=1    
    print(count1,count0,len(arr),arr)


    
def segregate_0and1_optimize(arr):
    start=0
    end=len(arr)-1
    while start<end:
        if arr[start]==0:
            start+=1
        else:
            if arr[end]==0:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
            else:
                end-=1
    print(arr)






segregate_0and1_optimize([0,1,1,0])