class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#Creating nodes
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.left.left=Node(3)
root.left.right=Node(7)
ch=0            #Initialize the choice variable
while(ch!=4):
    ch=int(input("\n\nEnter your choice:\n1.Inorder\t2.Preorder\t3.Postorder\t4.Exit: "))
    if ch==1:
        #Inorder Traversal
        def inorder(node):
            if node:
                inorder(node.left)
                print(node.data,end="\t")
                inorder(node.right)
        print("\nInorder Traversal:")
        inorder(root)
    elif ch==2:
        #Preorder Traversal
        def preorder(node):
            if node:
                print(node.data,end="\t")
                preorder(node.left)
                preorder(node.right)
        print("\nPreorder Traversal:")
        preorder(root)
    elif ch==3:
        #Postorder Traversal
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                print(node.data,end="\t")
        print("\nPostorder Traversal:")
        postorder(root)
    elif ch==4:
        print("Exiting...\n")
    else:
        print("Wrong choice, please try again!!")
