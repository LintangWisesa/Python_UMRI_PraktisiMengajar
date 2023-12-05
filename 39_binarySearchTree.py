# binary search tree: 
# 0. binary tree (max 2 children per node)
# 1. left nodes < root
# 2. right node > root

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def insert(node, val):
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    return node

root = None
root = insert(root, 8)
insert(root, 3)
insert(root, 10)
insert(root, 1)
insert(root, 6)
insert(root, 4)
print(root)

def search(root, val):
    if root is None or root.val == val:
        return root
    if val > root.val:
        return search(root.right, val)
    else:
        return search(root.left, val)

cari = 5
if search(root, cari) is None:
    print("Not found")
else:
    print(cari, " found")


