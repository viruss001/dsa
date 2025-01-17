def lcmoftwonumber(a,b):
    if a>b:
        greater=a
    else :
        greater=b
    while(True):
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    print( lcm)

lcmoftwonumber(2,3)