# given n we hafe to find whole row
def wholerow(n):
    col=1
    ans=1
    print(1)
    while(n-1>0):
        ans=ans*n//col
        print(ans)
        n=n-1
        col+=1
    print(1)
wholerow(5)