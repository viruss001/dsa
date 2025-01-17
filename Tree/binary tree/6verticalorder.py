from Tree import Creating, Node
root = Node(None)
root=Creating(root)




def vertical(root,h,v):
    if root is None :
        return {}
    
    if root.left is None and root.right is None:
        return {h:[{v:[root.data]}]}
   
    left=vertical(root.left,h-1,v+1)
    right=vertical(root.right,h+1,v+1)
    ans={**left,**right}
    keylist=list(ans.keys())
    if h in keylist:
    #    when it is on same level then it create a problem
        keyss=[]
        for i in ans[h]:
            print(i,"i")
            keyss.extend(i.keys())
        print(keyss,"keyss" , v)
        print(v in keyss,"v in keyss")
        if v in keyss:
            print(v in keyss,"v in keyss")
            print(keyss,"keyss")
            for j in ans[h]:

                if v in j.keys():
                    print(v in j.keys())
                    j[v].append(root.data)


        else:
            ans[h].append({v:[root.data]})
    else:
      
        temp={h:[{v:[root.data]}]}
        ans={**ans,**temp}
    return ans

a =vertical(root,0,1)
print(a)