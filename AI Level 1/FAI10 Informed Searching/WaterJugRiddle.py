# main.py

import queue
class Node:
  def __init__(self,Jug3L,Jug5L):
    self.neighbors = []
    self.water = (Jug3L,Jug5L)

  def add_neighbor(self,node):
    self.neighbors.append(node)

  def __str__(self):
    return f'3 Liter Jug: {self.water[0]}, 5 Liter Jug: {self.water[1]}'

  def __eq__(self,other):
    return self.__class__==other.__class__ and self.water == other.water
  
  def __lt__(self,other):
    return self.water < other.water
  
  def __hash__(self):
    return int(str(self.state[0])+str(self.state[1]))
  
  def is_solved(self):
    return self.water[1] == 4
  
  def generate_neighbors(self):
    self.neighbors.append(Node(3,self.water[1]))
    self.neighbors.append(Node(self.water[0],5))
    self.neighbors.append(Node(self.water[0],0))
    self.neighbors.append(Node(0,self.water[1]))
    if self.water[1]+self.water[0]>=5:
      self.neighbors.append(Node(self.water[0]-(5-self.water[1]),5))
    else:
      self.neighbors.append(Node(0,self.water[1]+self.water[0]))

    if self.water[1]+self.water[0]>=3:
      self.neighbors.append(Node(3,self.water[1]-(3-self.water[0])))
    else:
      self.neighbors.append(Node(self.water[1]+self.water[0],0))

  def get_heuristic(self):
    if self.is_solved():
      return 0
    else: 
      return abs(self.water[0] + self.water[1] - 4)

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

  def __str__(self):
    nodegraph = ""
    for i in self.graph:
      nodegraph += f'{self.graph[i]}\n'
    return nodegraph
