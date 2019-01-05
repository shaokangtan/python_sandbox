class Node:

    def __init__(self, value):
        self.value = value
        self.next_node  = None

    # return found node, else return None
    def find(self, node):
        h = self
        while h!= None:
            if h == node:
                return h
            h = h.next_node
        return h

    # return removed node, else return None
    def remove(self, node):
        h = self
        pre_h = None
        while h!= None:
            if h == node:
                pre_h.next_node = node.next_node
                return h
            pre_h = h
            h = h.next_node
        return h

    def add_node(self, node):
        if self.next_node == None:
            self.next_node = node
        else:
            h = self
            while h.next_node:
                if h == node:
                    print ("warning: duplicated node {} found".find(node))
                h = h.next_node
            h.next_node = node

    def __str__(self):
        h = self
        while h!= None:
            #return  "{}:{} ".format(h, h.value)
            return str(type(h)) + " " + str (id(h)) + ":" + str(h.value)
            h = h.next_node

    def print(self):
        h = self
        while h!= None:
            print("{} ".format(h))
            h = h.next_node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.add_node(b)
b.add_node(c)
c.add_node(d)
d.add_node(e)
a.add_node(f)

def nth_to_last_node(n, head):

    left_pointer  = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n-1):

        # Check for edge case of not having enough nodes!
        if not right_pointer.next_node:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.next_node

    # Move the block down the linked list
    while right_pointer.next_node:
        left_pointer  = left_pointer.next_node
        right_pointer = right_pointer.next_node

    # Now return left pointer, its at the nth to last element!
    return left_pointer



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
# This would return the node d with a value of 4, because its the 2nd to last node.
#target_node = nth_to_last_node(2, a)
print ("answer={}".format(nth_to_last_node(2, a).value))


if a.find(c):
    print ("found node: {} vale: {}".format(c, c.value))
else:
    print ("cannot find node: {} vale: {}".format(c, c.value))

if a.remove(c):
    print ("Removed node: {} vale: {}".format(c, c.value))

if a.find(c):
    print ("found node: {} vale: {}".format(c, c.value))
else:
     print ("cannot find node: {} vale: {}".format(c, c.value))

print ("{}".format(a))

a.print ()