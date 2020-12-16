from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
   def util(self,M,u,v):
      M[u][v]=1
      for i in self.graph[v]:
         if M[u][i]==0:
            self.util(M,u,i)
   def transitive_closure(self):
      M=[[0 for j in range(self.vertex)] for i in range(self.vertex)]
      for i in range(self.vertex):
         self.util(M,i,i)
      print(M)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("The transitive closure of the graph is")
   graph.transitive_closure()

