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

  def greedy_search(self,initial):
    visitable = queue.PriorityQueue()
    visited = set()
    visitable.put((0,initial))
    node = initial
    while not visitable.empty():
      cost,node = visitable.get()
      if node not in visited:
        print(node.key,end=' ')
        visited.add(node)
        for i in node.neighbors:
          if self.graph[i] not in visited:
            visitable.put((node.neighbors[i],self.graph[i]))


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
g.add_edge(a, b, 3)
g.add_edge(a, c, 5)
g.add_edge(a, e, 15)
g.add_edge(b, d, 2)
g.add_edge(b, e, 6)
# run greedy search
# expected output: a b d c e
g.greedy_search(a)