# tree: hierarchical data structure consist of NODES (has its value) and EDGES
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# create node
root = Node(55)
root.left = Node(20)
root.left.left = Node(10)
root.left.right = Node(25)
root.right = Node(78)
root.right.right = Node(90)

def inorder(root): # kiri - root - kanan
    if root:
        inorder(root.left)
        print(str(root.val), end=" - ")
        inorder(root.right)

def preorder(root): # root - kiri - kanan
    if root:
        print(str(root.val), end=" - ")
        preorder(root.left)
        preorder(root.right)

def postorder(root): # kiri - kanan - root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val), end=" - ")

print("\nInorder traversal: ")
inorder(root)
print("\nPreorder traversal: ")
preorder(root)
print("\nPostorder traversal: ")
postorder(root)

