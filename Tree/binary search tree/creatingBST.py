class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data=data
        self.right=right
        self.left=left
        

def insertIntoBST(root,data):
    if root is None:
        temproot=Node(data)
        return temproot
    if data>root.data:
        root.right=insertIntoBST(root.right,data)
    else :
        root.left=insertIntoBST(root.left,data)
    return root
def creatingBst():
    root=None
    print("now create a tree")
    data=int(input("Enter the data "))
   # print(data)
    while data is not -1:
        root = insertIntoBST(root,data)
        #print(data)
        data=int(input("Enter the data "))
    print("Your tree is created")

creatingBst()