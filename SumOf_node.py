class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def SumOf_node(root):
    if root==None:
        return 0
    return (root.data +SumOf_node(root.left)+ SumOf_node(root.right))

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
btn1= BinaryTreeNode(10)
btn2= BinaryTreeNode(20)
btn3= BinaryTreeNode(30)
btn4= BinaryTreeNode(40)
btn5= BinaryTreeNode(50)
btn6= BinaryTreeNode(60)
btn7= BinaryTreeNode(70)

#make connection
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
btn3.left=btn6
btn3.right=btn7
PrintTree(btn1)
print("Sum Of All Node :",SumOf_node(btn1)) #function call