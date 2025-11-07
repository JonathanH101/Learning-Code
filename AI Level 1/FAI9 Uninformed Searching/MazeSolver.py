# main.py
import maze as mz
import queue

# construct maze
# X is goal (located at (2, 0))
# O is the player (we'll start at (0, 0))
# * are cells with quicksand (higher cost to travel from this cell to another)
maze = ""
maze += "+---+---+---+\n"
maze += "|           |\n" # row0
maze += "+   +---+   +\n"
maze += "|     * |   |\n" # row1
maze += "+---+   +   +\n"
maze += "| X         |\n" # row2
maze += "+---+---+---+\n"
      # col0 col1 col2

# row has 14 characters (including new line) so maze width is 14

maze = mz.Maze(maze, 14)
maze.print_maze()


class Node:
  # modified to store Node state and dictionary of neighbors mapping neighbor node's keys to the weight from the current node to that neighbor
  def __init__(self, key):
    self.key = key
    self.neighbors = {}

  # modified to take in edge weight and update neighborst dictionary
  def add_neighbor(self, node, weight):
    self.neighbors[node.key] = weight

  # modified to print state and key value pairs in neighbors
  def __str__(self):
    s = "ID: " + self.key + "\nNeighbors: "
    for n in self.neighbors:
      s += n + ":" + str(self.neighbors[n]) + "  "
    return s

  def __lt__(self,other):
    return self.key < other.key

class Graph:

  def __init__(self):
    self.graph = {}

  def add_node(self, node):
    self.graph[node.key] = node

  # modified to create directed edges and take in a weight for the edge
  def add_edge(self, node1, node2, weight):
    if not node1.key in self.graph:
      print("Node with ID " + node1.key + " is not in the graph")
    elif not node2.key in self.graph:
      print("Node with ID " + node2.key + " is not in the graph")
    else:
      node1.add_neighbor(node2, weight)

  def __str__(self):
    s = ""
    for node in self.graph:
      s += self.graph[node].__str__() + "\n\n"
    return s

  def get_ucs_path(self,start,end):
    visitable = queue.PriorityQueue()
    visited = set()
    visitable.put((0,start,[start.key]))
    while not visitable.empty():
      cost,node,path = visitable.get()
      if node not in visited:
        if node == end:
          return path
        visited.add(node)
        print(node.key)
        print(cost)
        for i in node.neighbors:
          if self.graph[i] not in visited:
            visitable.put((node.neighbors[i]+cost,self.graph[i],path+[self.graph[i].key]))



  def get_dls_path(self,initial,limit,end):
    visited = {initial}
    visitable = [(initial,0,[initial.key])]
    while len(visitable) != 0:

      node,depth,path = visitable.pop()
      print(node.key,end=' ')

      if node == end:
        return path

      for i in node.neighbors:
        if depth+1 <= limit and i not in visited:
          visited.add(i)
          visitable.append((i,depth+1,path+[i]))

  def get_ids_path(self,start_node,max_depth,end):
    for i in range(max_depth+1):
      path = self.get_dls_path(start_node,i,end)
      if path != None:
        return path




  def get_bfs_path(self,start,end):
    queue = [(start,[start.key])]
    visited = {start}
    while len(queue) != 0:
      for i in queue:
        print(i.key)
      a,path = queue.pop(0)
      if a == end:
        return path
      print(a)
      for i in a.neighbors:
        if i not in visited:
          queue.append((self.graph[i],path+[i]))
          visited.add(i)

  def get_dfs_path(self,start,end):
    stack = [(start,[start.key])]
    visited = {start}
    while len(stack) != 0:
      a,path = stack.pop()
      if a == end:
        return path
      visited.add(a)
      print(a)
      for i in a.neighbors:
        if self.graph[i] not in visited:
          stack.append((self.graph[i],path+[i]))

  def get_path_cost(self,path):
    total = 0
    node =
    for i in path:
      node2 = self.graph[i]
      total +=
# construct graph of the maze
# names are "nodexy" where x is the row of the cell, y is the column of the cell
node00 = Node("(0,0)")
node01 = Node("(0,1)")
node02 = Node("(0,2)")
node10 = Node("(1,0)")
node11 = Node("(1,1)")
node12 = Node("(1,2)")
node20 = Node("(2,0)")
node21 = Node("(2,1)")
node22 = Node("(2,2)")

g = Graph()
g.add_node(node00)
g.add_node(node01)
g.add_node(node02)
g.add_node(node10)
g.add_node(node11)
g.add_node(node12)
g.add_node(node20)
g.add_node(node21)
g.add_node(node22)

g.add_edge(node00, node10, 1)
g.add_edge(node00, node01, 1)

g.add_edge(node01, node00, 1)
g.add_edge(node01, node02, 1)

g.add_edge(node02, node01, 1)
g.add_edge(node02, node12, 1)

g.add_edge(node10, node00, 1)
g.add_edge(node10, node11, 1)

g.add_edge(node11, node21, 10)
g.add_edge(node11, node10, 10)

g.add_edge(node12, node02, 1)
g.add_edge(node12, node22, 1)

g.add_edge(node20, node21, 1)

g.add_edge(node21, node20, 1)
g.add_edge(node21, node11, 1)
g.add_edge(node21, node22, 1)

g.add_edge(node22, node21, 1)
g.add_edge(node22, node12, 1)

# different types of traversals to find path to goal
dfs = g.get_dfs_path(node00, node20)
print(dfs)
maze.print_path(dfs)
g.get_path_cost(dfs)
print()

bfs = g.get_bfs_path(node00, node20)
print(bfs)
maze.print_path(bfs)
g.get_path_cost(bfs)
print()

ids = g.get_ids_path(node00, node20, 6)
print(ids)
maze.print_path(ids)
g.get_path_cost(ids)
print()

ucs = g.get_ucs_path(node00, node20)
print(ucs)
maze.print_path(ucs)
g.get_path_cost(ucs)
print()