levels = []
level = 0;
def collect_tree_oder(tree, l):
    if tree != None:
        if len(levels) == l:
            levels.append([tree.value]) # add new level L
        else:
            levels[l].append(tree.value) # add new node to the level l
        collect_tree_oder(tree.left,l+1)
        collect_tree_oder(tree.right,l+1)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

from node import *

def print_tree_oder(root):
    global levels
    levels.clear()
    collect_tree_oder(root, 0)
    for l in levels:
        print (l)

