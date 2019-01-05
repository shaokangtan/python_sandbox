class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


def reverse_linked_list(node):
    current = node
    prev = None
    next = None

    while current:
        next = current.nextnode
        current.nextnode = prev
        prev = current
        current = next

a = Node(1)
b = Node(2)
c = Node (3)
d = Node (4)
a.nextnode = b
b.nextnode = c
c.nextnode = d

def print_linked_list(node):
    while (node):
        print ("{} ".format(node.value))
        node = node.nextnode

print_linked_list(a)

print ("reverse linked list")
reverse_linked_list(a)

print_linked_list(d)