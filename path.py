import inspect, os
print (inspect.stack()[0][1])
stack_size = len(inspect.stack()[0])
for st in range(stack_size-1):
    print ("{}:{}".format(st, inspect.stack()[st][1]))

print(os.path.realpath(__file__))
print (inspect.currentframe())
print (inspect.getfile(inspect.currentframe())) # script filename (usually with path)
print (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) # script directory

p = os.path.dirname(__file__)

"""
 /A, /B, /C
 /A/abc
 /A/abc/def
 
 / children: A, B, C
 /A children: abc
 /A/abc children: def
"""
class Directory:
    def __init__(self, name=""):
        self.name = name
        self.children = {}

def build_dirs(tree, path):
    dirs = path.split("/")
    print (dirs)
    if tree == None:
        tree = Directory("root")
    t = tree
    for d in dirs:
        while d in t.children:
            t = t.children[d]
            continue
        new_directory = Directory(d)
        t.children[d] = new_directory
    return tree


tree = build_dirs(None,p)

stack = [tree]
while len(stack):
    children = stack.pop(0).children
    for k, v in children.items():
        print (k)
        stack.append(v)
