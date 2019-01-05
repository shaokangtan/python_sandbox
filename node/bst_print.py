#demostrate breadth first, depth first path
from node import Node

levels = []

def collect_tree_oder1(tree, l):
    if tree != None:
        if len(levels) == l:
            levels.append([tree.value]) # add new level L
        else:
            levels[l].append(tree.value) # add new node to the level l
        collect_tree_order1(tree.left,l+1)
        collect_tree_order1(tree.right,l+1)

levels = []
def collect_tree_order(tree, l):
    if tree == None:
        return
    if len(levels) == l:
        levels.append([tree.value])
    else:
        levels[l].append(tree.value)
    collect_tree_order(tree.left, l+1)
    collect_tree_order(tree.right, l+1)


def print_tree_order(root):
    global levels
    levels.clear()
    collect_tree_order(root, 0)
    for l in levels:
        print (l)

#collect each end node path
def collect_branch_information(tree, branch_list, cur_list,  l):
    if tree != None:
        if l ==0:
            cur_list.append(tree)
        if tree.right:
            new_list = cur_list[:]
            branch_list.append(new_list)
            new_list.append(tree.right)
            collect_branch_information(tree.right, branch_list, new_list, l+1)
        if tree.left:
            cur_list.append(tree.left)
            collect_branch_information(tree.left, branch_list, cur_list, l+1)
def collect_branch_information_1(tree, branch_list, cur_list, l): #dfs
    if tree != None:
        cur_list.append(tree)
        collect_branch_information_1(tree.left, branch_list, cur_list,l+1) 
        collect_branch_information_1(tree.right, branch_list, cur_list,l+1)
        if tree.right == None and tree.left == None:
            branch_list.append(cur_list[:]) # end of branch
        cur_list.pop()
def print_branch_information(root):
    cur_list = []
    branch_list = [cur_list]
    collect_branch_information(root, branch_list, cur_list, 0)
    for b in branch_list:
        for n in b:
            print ("{} ".format( n.value), end="")
        print()
    cur_list = []
    branch_list = []
    collect_branch_information_1(root, branch_list, cur_list, 0)
    for b in branch_list:
        for n in b:
            print ("{} ".format( n.value), end="")
        print()    

if __name__ == '__main__':
    levels.clear()
    root = Node(7)
    root.left = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(5)
    root.right = Node(11)
    root.right.left = Node(9)
    root.right.right = Node( 15)
    root.right.right.left = Node(13)
    root.right.right.right = Node(17)

    print_tree_order(root)
    print_branch_information(root)

