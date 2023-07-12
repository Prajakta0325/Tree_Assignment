class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

'''def PrintTree(root):
    if root==None:
        return
    print(root.data) #it will print root node i.e. 100
    PrintTree(root.left) #it will print all left side node through recurrcussion
    PrintTree(root.right) #it will print all right side node through recurrcussion'''

def PrintTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if  root.left != None:
        print("L",root.left.data,end=",")
    if root.right != None:
        print("R",root.right.data,end=",")
    print()
    PrintTree(root.left)
    PrintTree(root.right)

#create node
btn1= BinaryTreeNode(100)
btn2= BinaryTreeNode(54)
btn3= BinaryTreeNode(150)
btn4= BinaryTreeNode(27)
btn5= BinaryTreeNode(80)
btn6= BinaryTreeNode(125)
btn7= BinaryTreeNode(185)

#make connection
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
btn3.left=btn6
btn3.right=btn7
PrintTree(btn1)