from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def addedges(self,u,v):
       self.graph[u].append(v)

   def util(self,u,color):
       color[u]="grey"
       for i in self.graph[u]:
          if color[i]=="white":
             if self.util(i,color):
                return True
          elif color[i]=="grey":
               return True
       color[u]="black"
       return False

   def iscyclic(self):
      color=["white"]*self.vertex
      for i in range(self.vertex):
          if color[i]=="white":
             if self.util(i,color):
                print(color)
                return True
      print(color)
      return False

if __name__=="__main__":
   graph=Graph(4)
   graph.addedges(0,2)
   graph.addedges(2,0)
   graph.addedges(0,1)
   graph.addedges(1,2)
   graph.addedges(2,3)
   print(graph.iscyclic())
   

