#given r and c tell which element at that place r=5,c=3


# formula is rCc r!/r!*(r-c)!
def nCr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    print(res)
r=5
c=3
nCr(r-1,c-1)