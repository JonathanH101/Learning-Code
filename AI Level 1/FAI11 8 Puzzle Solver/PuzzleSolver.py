import time 
from queue import PriorityQueue

class Node:
  def __init__(self, start):
    self.neighbors = []
    self.graph = start

  def __str__(self):
    return f'{self.graph[0][0]} {self.graph[0][1]} {self.graph[0][2]} \n{self.graph[1][0]} {self.graph[1][1]} {self.graph[1][2]} \n{self.graph[2][0]} {self.graph[2][1]} {self.graph[2][2]}'

  def __eq__(self,other):
    return self.__class__==other.__class__ and self.graph == other.graph
  
  def __lt__(self,other):
    return self.graph < other.graph
  
  def __hash__(self):
    number = ''
    for i in self.graph:
      for j in i:
        if j != ' ':
          number += j
        else:
          number += '0'
            
    return int(number)
  
  def is_solved(self):
    number = self.__hash__()
    return number == 123456780
  
  def generate_neighbors(self):
    
  
node1 = Node([['1','2','3'],['4','5','6'],['7','8',' ']])
print(node1.is_solved())