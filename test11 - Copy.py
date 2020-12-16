from collections import defaultdict
import argparse

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
      self.graph[u].append(v)

   def util(self,visited,path,u,v):
       visited[u]=True
       path.append(u)
       if u==v:
          print(path)
       else:
          for i in self.graph[u]:
             if not visited[i]:
                self.util(visited,path,i,v)
       path.pop()
       visited[u]=False

   def find_path(self,u,v):
       path=[]
       visited=[False]*self.vertex
       self.util(visited,path,u,v)

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("--vertex1",help="Enter Vertex1")
   parser.add_argument("--vertex2",help="Enter Vertex2")
   args=parser.parse_args()
   vertex1=int(args.vertex1)
   vertex2=int(args.vertex2)
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(1,2)
   graph.add_edges(0,1)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.add_edges(1,3)
   graph.find_path(vertex1,vertex2)
