class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def cycle_check(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:

        # Note
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False

def cycle_check_2(node):
    node_list = {}
    while node.nextnode != None:
        # print("{}".format(id(node)))
        if id(node) in node_list:
            return True
        node_list[id(node)] = 1
        node = node.nextnode
    return False
if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e
    e.nextnode = f
    f.nextnode = f
    print ("{}".format(cycle_check_2(a)))
