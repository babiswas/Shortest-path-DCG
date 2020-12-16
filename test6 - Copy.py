from collections import defaultdict
import argparse

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edge(self,u,v):
       self.graph[u].append(v)
   def util(self,visited,u):
       visited[u]=True
       print(u)
       for i in self.graph[u]:
          if not visited[i]:
            self.util(visited,i)
   def DFS(self):
      visited=[False]*self.vertex
      for i in range(self.vertex):
         if not visited[i]:
            self.util(visited,i)

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("edge0",help="Enter vertex")
   parser.add_argument("edge1",help="Enter vertex")
   parser.add_argument("edge2",help="Enter vertex")
   parser.add_argument("edge3",help="Enter vertex")
   args=parser.parse_args()
   edge0=int(args.edge0)
   edge1=int(args.edge1)
   edge2=int(args.edge2)
   edge3=int(args.edge3)
   graph=Graph(4)
   graph.add_edge(edge0,edge1)
   graph.add_edge(edge0,edge2)
   graph.add_edge(edge3,edge3)
   graph.add_edge(edge2,edge3)
   graph.add_edge(edge2,edge0)
   graph.add_edge(edge1,edge2)
   graph.DFS()
