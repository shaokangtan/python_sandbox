'''
use 2 stacks to implement a queue
'''
class Queue2Stacks_2N(object):

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):

        # FILL OUT CODE HERE
        self.stack1.append(element)

    def dequeue(self):
        # FILL OUT CODE HERE
        self.stack2 = self.stack1[::-1]
        ans =  self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        return ans

class Queue2Stacks_N(object):

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):

        # FILL OUT CODE HERE
        self.stack1.append(element)

    def dequeue(self):
        # FILL OUT CODE HERE
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return None
            else:
                self.stack2 = self.stack1[::-1]
                ans = self.stack2.pop()
                self.stack1.clear()
                return ans
        else:
            return self.stack2.pop()
        return ans

'''
    Check if Queue is Empty
    Enqueue
    Dequeue
    Return the size of the Queue
    class Queue(object):
'''
class Queue(object):
    def __init__(self):
        self.queue = []
    def Enqueue(self, element):
        self.queue.append(element)
    def Dequeue(self):
        return self.queue.pop(0)
    @property
    def size(self):
        return len(self.queue)

q = Queue()
print (q.size)
for i in range(5):
    q.Enqueue(i)
for i in range(5):
    print("Dequeue:{} size:{}".format(q.Dequeue(), q.size))



q = Queue2Stacks_N()
for i in range (5):
    q.enqueue(i)
for i in range (6):
    print (q.dequeue())
for i in range (3):
    q.enqueue(i)
for i in range (6):
    print (q.dequeue())
