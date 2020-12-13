from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def is_cyclic_util(self,u,visited,recstack):
       recstack[u]=True
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             if self.is_cyclic_util(i,visited,recstack):
                return True
          elif recstack[i]==True:
               return True
       recstack[u]=False
       return False

   def is_cyclic(self):
       visited=[False]*self.vertex
       recstack=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
             if self.is_cyclic_util(i,visited,recstack):
                return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   print(graph.is_cyclic())
   print("Creating another graph")
   graph1=Graph(4)
   graph1.add_edges(2,0)
   graph1.add_edges(0,2)
   graph1.add_edges(2,3)
   graph1.add_edges(0,1)
   graph1.add_edges(1,2)
   print(graph1.is_cyclic())

       
