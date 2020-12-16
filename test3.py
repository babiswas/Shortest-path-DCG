from collections import defaultdict
import argparse

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
               visited[i]=True

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("num",help="Enter entry vertex",type=int)
   args=parser.parse_args()
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("Starting BFS tarversal")
   graph.BFS(args.num)


   