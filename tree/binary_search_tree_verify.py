# Python program to check if a binary tree is bst or not

# Method 1
#INT_MAX = 4_294_967_296
INT_MAX=float("inf")
#INT_MIN = -4_294_967_296
INT_MIN =float("-inf")

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data-1) and
            isBSTUtil(node.right, node.data+1, maxi))

# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
    print ("Is BST")
else:
    print ("Not a BST")


root = Node(40)
root.left = Node(20)
root.right = Node(50)
root.right.left = Node(15)
root.left.left = Node(10)
root.left.right = Node(30)

if (isBST(root)):
    print ("Is BST")
else:
    print ("Not a BST")

#method 2
binary_list = []
def inorder(tree):
    if tree!=None:
        inorder(tree.left)
        binary_list.append(tree.data)
        inorder(tree.right)

root = Node(40)
root.left = Node(20)
root.right = Node(50)
#root.right.left = Node(15)
root.left.left = Node(10)
root.left.right = Node(30)

binary_list.clear()
inorder(root)

if binary_list == sorted(binary_list):
    print ("Is BST")
else:
    print ("Is not BSF")
