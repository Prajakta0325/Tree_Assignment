class BinaryTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#pre order ==> root - left Node - right node

def pre_order(root):
    if root==None:
        return
    print(root.data,end=" ")
    pre_order(root.left)
    pre_order(root.right)

# post Order ==> left node - right node - root
def post_order(root):
    if root ==None:
        return 
    post_order(root.left)
    post_order(root.right)
    print(root.data,end=" ")

# inorder ==> left root right
def inoreder(root):
    if root == None:
        return 
    inoreder(root.left)
    print(root.data,end=" ")
    inoreder(root.right)
    

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
#pre_order(btn1)
#post_order(btn1)
inoreder(btn1)