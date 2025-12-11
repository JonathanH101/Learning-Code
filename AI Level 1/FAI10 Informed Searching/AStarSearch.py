# main.py

import queue
class Node:
  def __init__(self,key):
    self.key = key
    self.neighbors = {}

  def add_neighbor(self,node,cost):
    self.neighbors[node.key] = cost

  def __str__(self):
    nodes = ""
    nodes += f'ID: {self.key} \n'
    nodes += "Neighbors: "
    for i in self.neighbors:
      nodes += f'{i.key}, '
    return nodes

class Graph:
  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    self.graph[node.key] = node

  def add_edge(self, node1, node2, cost):
    if node1.key not in node2.neighbors and node2.key not in node1.neighbors:
      node1.add_neighbor(node2,cost)
      node2.add_neighbor(node1,cost)
    else:
      print("These nodes already share an edge!")

  def AStar(self,initial):
    visitable = queue.PriorityQueue()
    visited = set()
    visitable.put((0,0,initial,0))
    #^ f value, cost, node, depth ^
    node = initial
    while not visitable.empty():
      f,cost,node,depth = visitable.get()
      if node not in visited:
        print(node.key,end=' ')
        visited.add(node)
        for i in node.neighbors:
          if self.graph[i] not in visited:
            f = (2-depth)+(node.neighbors[i]+cost)
            visitable.put((f,node.neighbors[i]+cost,self.graph[i],depth+1))


  def __str__(self):
    nodegraph = ""
    for i in self.graph:
      nodegraph += f'{self.graph[i]}\n'
    return nodegraph


# construct Graph
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
g = Graph()
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)
g.add_edge(a, b, 2)
g.add_edge(a, c, 1)
g.add_edge(e, d, 1)
g.add_edge(c, d, 1)
g.add_edge(b, e, 3)
# run a star search
# expected output: a c d e b
g.AStar(a)