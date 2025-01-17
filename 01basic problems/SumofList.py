def sumOflist(arr):
    s=0
    for i in arr:
        s+=i
    return s


def mulOflist(arr):
    s=1
    for i in arr:
        s*=i
    return s
arr=[1,2]
print(sumOflist(arr))
print(mulOflist(arr))