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
    return int(str(self.water[0])+str(self.water[1]))
  
  def is_solved(self):
    return self.water[1] == 4
  
  def generate_neighbors(self):
    self.neighbors.append(Node(3,self.water[1]))
    self.neighbors.append(Node(self.water[0],5))
    if not self.water[0]+self.water[1] == 0:
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
      if abs(self.water[0] + self.water[1] - 4) == 0:
        return 1
      else:
        return abs(self.water[0] + self.water[1] - 4)

class Graph:
  def __init__(self, initial):
    self.start = initial

  def Greedy(self):
    visitable = queue.PriorityQueue()
    visited = set()
    visitable.put((self.start.get_heuristic(),self.start,[self.start]))
    node = self.start
    num_states = 0
    while True:
      _,node,states = visitable.get()
      if node not in visited:
        num_states+=1
        if not node.is_solved():
          visited.add(node)
          node.generate_neighbors()
          for i in node.neighbors:
            if i not in visited:
              visitable.put((i.get_heuristic(),i,states+[i]))
        else:
          return states, num_states
        
  def AStar(self):
    visitable = queue.PriorityQueue()
    visited = set()
    visitable.put((self.start.get_heuristic(),self.start,[self.start],0))
    node = self.start
    num_states = 0
    while True:
      _,node,states,depth = visitable.get()

      if node not in visited:
        num_states+=1
        if not node.is_solved():
          visited.add(node)
          node.generate_neighbors()
          for i in node.neighbors:
            if i not in visited:
              visitable.put((depth+1+i.get_heuristic(),i,states+[i],depth+1))
        else:
          return states, num_states
      # visitable = queue.PriorityQueue()
      # visited = set()
      # visitable.put((0,0,self.start,0))
      # #^ f value, cost, node, depth ^
      # node = self.start
      # while not visitable.empty():
      #   f,cost,node,depth = visitable.get()
      #   if node not in visited:
      #     print(node.key,end=' ')
      #     visited.add(node)
      #     for i in node.neighbors:
      #       if self.graph[i] not in visited:
      #         f = (2-depth)+(node.neighbors[i]+cost)
      #         visitable.put((f,node.neighbors[i]+cost,self.graph[i],depth+1))

start = Node(0,0)
g = Graph(start)
print('Running Greedy Search...')
path, num_states = g.Greedy()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)
print()

print('Running A* Search...')
path, num_states = g.AStar()
print('Number of States Searched: ' + str(num_states))
print('Solution: ')
for node in path:
  print(node)