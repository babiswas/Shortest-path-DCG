from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def DFS_util(self,u,visited):
       visited[u]=True
       print(u)
       for i in self.graph[u]:
          if not visited[i]:
             self.DFS_util(i,visited)

   def DFS(self):
      visited=[False]*self.vertex
      for i in range(self.vertex):
         if not visited[i]:
            self.DFS_util(i,visited)

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.DFS()

     