from collections import defaultdict
import argparse
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
   def DFS(self,u):
       stack=[]
       visited=[False]*self.vertex
       stack.append(u)
       while stack:
           m=stack.pop(0)
           if visited[m]==False:
              print(m)
              visited[m]=True
           for i in self.graph[m]:
              if not visited[i]:
                 stack.append(i)

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("num",help="Enter the entry for DFS",type=int)
   args=parser.parse_args()
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("Starting dfs traversal")
   graph.DFS(args.num)

   

