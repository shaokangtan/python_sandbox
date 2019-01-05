# demo post order and pre order traverse
# trim node < min and node > max
from node.node import *

#import sys
#import os
#sys.path.append(os.path.abspath("C:/Users/shaok/IdeaProjects/python_sandbox/tree"))
from  node.bst_print import *


root = Node(7)
root.left = Node(4)
root.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(11)
root.right.left = Node(9)
root.right.right = Node( 15)
root.right.right.left = Node(13)
root.right.right.right = Node(17)

n=0
#prev order traverse
def trim_bst(node, min, max):
    global n
    n += 1
    if min > max:
        raise ( "min > max ")
    assert (min <= max)
    if node.value< min:
        if node.right == None:
           print ( "node %d out of  %d and %d" % (node.value, min, max))
           return None
        else:
            return trim_bst(node.right, min, max)

    if node.value > max:
        if node.left  == None:
            print ( "node %d out of  %d and %d" % (node.value, min, max))
            return None
        else:
            return trim_bst(node.left, min, max)

    if node.left != None:
        print (" go to left node %d" % node.left.value )
        node.left = trim_bst(node.left, min, max)
    if node.right!= None:
        print (" go to right node %d" % node.right.value )
        node.right = trim_bst(node.right, min, max)
    return node

#post order traverse
def trimBST(tree, minVal, maxVal):
    global n
    n += 1
    if not tree:
        return

    tree.left=trimBST(tree.left, minVal, maxVal)
    tree.right=trimBST(tree.right, minVal, maxVal)

    if minVal <= tree.value <= maxVal:
        return tree

    if tree.value<minVal:
        return tree.right

    if tree.value>maxVal:
        return tree.left

print_bst (root)
try:
    #root1 = trim_bst(root, 4, 15)
    #root1 = trim_bst(root, 8, 15)
    root2 = trimBST(root,8,15)
    #root1 = trim_bst(root, 18, 19)
    #root1 = trim_bst(root, 20, 19)
except  Exception as e:
    print(e, type(e))
else:
    print ("result")
    print_bst (root)
    print ("n = {}".format(n))

