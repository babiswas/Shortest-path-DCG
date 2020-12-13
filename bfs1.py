from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
   def BFS(self,u):
     queue=[]
     visited=[False]*self.vertex
     queue.append(u)
     visited[u]=True
     while queue:
         m=queue.pop(0)
         print(m)
         for i in self.graph[m]:
           if not visited[i]:
              queue.append(i)
              visited[i]=False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.BFS(2)
