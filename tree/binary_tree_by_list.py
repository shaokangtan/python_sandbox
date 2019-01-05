
#Tree Representation Implementation (Lists)

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

root = BinaryTree("parent")
right = BinaryTree("right child")
left = BinaryTree("left child")
insertLeft(root, left)
insertRight(root, right)
print (root)
print (getRootVal(root))
insertRight(root, "new right child")
print (root)
child = getRightChild(root)
print (getRootVal(child))
print (child)
child = getRightChild(child)
print (getRootVal(child))
#setRootVal(child, "right child -> new left grandchild")
#print (root)