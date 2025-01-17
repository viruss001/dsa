def setMatrixZero(matrix):
    n=len(matrix)
    m=len(matrix[0])
    colarr=[0]*m
    rowarr=[0]*n
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                colarr[j]=1
                rowarr[i]=1
    print( rowarr,colarr)

    for i in range(n):
        for j in range(m):
            if rowarr[i]==1 or colarr[j]==1:
                matrix[i][j]=0
    print(matrix)

matrix=[
    [1,1,1,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,0,0,1]
]
setMatrixZero(matrix)