from Tree import Creating, Node
root = Node(None)
root=Creating(root)




def vertical(root, h=0, v=0):
    if root is None:
        return {}
    
    # Recursive calls for left and right children
    left = vertical(root.left, h - 1, v + 1)
    right = vertical(root.right, h + 1, v + 1)
    
    # Combine left and right results
    ans = {**left, **right}
    
    # Ensure the current horizontal distance `h` exists in the dictionary
    if h not in ans:
        ans[h] = []
    
    # Check if there is an entry for the current vertical level `v` in `ans[h]`
    found = False
    for entry in ans[h]:
        if v in entry:
            entry[v].append(root.data)
            found = True
            break
    
    # If no entry for `v` exists, create a new one
    if not found:
        ans[h].append({v: [root.data]})
    
    return ans
a =vertical(root,0,1)
print(a)
