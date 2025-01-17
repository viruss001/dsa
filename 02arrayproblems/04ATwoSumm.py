def binarysearch(arr,key):
        s = 0
        e = len(arr) - 1
        while s <= e:
            m = s + (e - s) // 2

            if arr[m] == key:
                return [m]
            elif arr[m] > key:
                e = m - 1
            else:
                s = m + 1
        return None

def twosum(arr,target):
    for i in range(0,len(arr)):
        x=target-arr[i]
        print("x is",x)
        indexofx=binarysearch(arr[i+1:],x)
        # print(x,indexofx)
        if indexofx is not None:
            print(arr[i],indexofx)
            return
        


def two_sum_optimize(arr,target):
     s,e=0,len(arr)-1
     
     while s<e:
            sum=arr[s]+arr[e]
            if sum==target:
               print(arr[s],arr[e],s,e)
               return
            elif sum<target:
               s+=1
            else:
                e-=1

        
     
        
           


two_sum_optimize([1,4,45,6,10,8],5)