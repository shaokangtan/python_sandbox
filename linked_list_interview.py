'''
dobule linked list
'''
from nose.tools import assert_equal
class Node(object):
    def __init__(self, data=None):
        self.prev_node = None
        self.next_node = None
        self.data = data

    def next(self):
        return self.next_node

    def previous(self):
        return self.previous_node

    def data(self):
        return self.data

    def insert(self, new):
        n = self.next_node
        new.previous_node = self
        new.next_node = n
        self.next_node = new

    def print(self):
        n = self
        while n:
            print (n.data)
            n = n.next_node

    def remove(self,node):
        h = self
        prev = None
        next = None
        while h:
            prev = h.prev_node
            next  = h.next_node
            if h == node:
                if next:
                    next.prev = prev
                if prev:
                    prev.next = h.next
            h = h.next_node



class Node_sl(object):
    def __init__(self, data=None):
        self.next_node = None
        self.data = data

    def next(self):
        return self.next_node



    def data(self):
        return self.data

    def insert(self, new):
        new.next_node = self.next_node
        self.next_node = new


    def print(self):
        n = self
        while n:
            print (n.data)
            n = n.next_node



def test_Node():
    a = Node("a")
    b = Node("b")
    a.insert(b)
    a.Print()
    c = Node_sl("c")
    d = Node_sl("d")
    c.insert(d)
    c.Print()


#test_Node()

def nth_to_last_node(n, head):
    h1 = head
    h2 = head
    for i in range(n):
        h1 = h1.next_node
        if h1 == None:
            return None

    while h1:
        print (h1.data)
        print (h2.data)
        h1 = h1.next_node
        h2 = h2.next_node
    return h2


####
def test_NLast():
    class TestNLast(object):

        def test(self,sol):

            assert_equal(sol(2,a),d)
            print ('ALL TEST CASES PASSED')

    # Run tests
    a = Node_sl(1)
    b = Node_sl(2)
    c = Node_sl(3)
    d = Node_sl(4)
    e = Node_sl(5)

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e

    t = TestNLast()
    t.test(nth_to_last_node)

#test_NLast()

def reverse(head):
    prev = None
    current = head
    while current != None:
        next = current.next_node;
        current.next_node = prev
        prev = current
        current = next

    return prev

def test_reverse():
    #Create a list of 4 nodes
    a = Node_sl(1)
    b = Node_sl(2)
    c = Node_sl(3)
    d = Node_sl(4)
    h = reverse(a)
    h.print()

    # Set up order a,b,c,d with values 1,2,3,4
    a.next_node = b
    b.next_node = c
    c.next_node = d

    h = reverse(a)
    h.print()

test_reverse()

'''Singly Linked List Cycle Check'''

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

def cycle_check(head):
    if head == None:
        return False
    h1 = head
    h2 = head.next_node.next_node
    while h2:
        if h2 == h1:
            return True
        h1 = h1.next_node
        if h2.next_node == None:
            return False
        h2 = h2.next_node.next_node
    return False

def test_cycle_check():
    # CREATE CYCLE LIST
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = d # Cycle Here!


    # CREATE NON CYCLE LIST
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.next_node = y
    y.next_node = z


    #############
    class TestCycleCheck(object):

        def test(self,sol):
            assert_equal(sol(a),True)
            assert_equal(sol(x),False)

            print ("ALL TEST CASES PASSED")

    # Run Tests

    t = TestCycleCheck()
    t.test(cycle_check)

test_cycle_check()