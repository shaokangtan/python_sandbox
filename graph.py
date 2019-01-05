from enum import Enum

class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #Gray

from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight

def dfs(graph, start):
    it = 0
    visited, stack = set(), [start]
    while stack:
        it += 1
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    print ("dfs time complexity: {}".format(it))
    return visited

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

list = dfs(graph, 'A')
print (list)

#depth first search
def dfs_paths(graph, start, goal):
    it = 0
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print ("vertex:{}, graph[vertex]{} - path {}".format(vertex, graph[vertex], path))
        for nxt in graph[vertex] - set(path): # - set(path) to exlcude any previously visited node
            it += 1
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

    print ("dfs_PATH time complexity: {}".format(it))

#breadth first search
def bfs_paths(graph, start, goal):
    it = 0
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop(0)         # path contined visited vertex in the order of traverse
        for nxt in graph[vertex] - set(path): # avoid duplicated vertex already visit
            it += 1
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))
    print ("bfs_PATH time complexity: {}".format(it))

#for i in dfs_paths(graph, 'A', 'F'):
#    print (i)

#path_list = list(dfs_paths(graph, 'A', 'F'))

path_list = [i for i in dfs_paths(graph, 'A', 'F')]
print(path_list)

path_list= [i for i in bfs_paths(graph, 'A', 'F')]
print(path_list)

visit_list = dfs_recursive(graph, 'A')



g = Graph()
g.add_edge(0, 1, 5)
print (g.nodes)
g.add_edge(0, 2, 10)
g.add_edge(0, 3, 15)
print (g.nodes)
for i in g.nodes.items():
    print (i)
    num,node = i
    print (num)
    print (node)
    for k,v in node.adjacent.items():
        print ("key/num: {}, value/weight: {}".format(k,v))

