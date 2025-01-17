def multiplicationOfMatrix(arr1,arr2):
    c=[[0]*len(arr2[0])]*len(arr1)
    print(c)
    if len(arr1[0]) is len(arr2) :
        for i in range(0,len(arr1)):
            for j in range(0,len(arr2[0])):
                for k in range(0,len(arr2)):
                    c[i][j]+=arr1[i][k]*arr2[k][j]
    print(c)
    return c
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
# take a 3x4 matrix    
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
multiplicationOfMatrix(A,B)