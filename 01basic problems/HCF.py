def HCF(a,b):
    if a>b:
        smaller=b
    else:
        smaller=a
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf

a=HCF(2,4)
print(a)