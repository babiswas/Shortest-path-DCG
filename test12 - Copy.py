from collections import defaultdict
import argparse

class Graph:
   def __init__(self,vertex):
      self.vertex=vertex
      self.graph=defaultdict(list)
   def add_edges(self,u,v):
      self.graph[u].append(v)
   def BFS(self,u,level):
       count=0
       queue=[]
       visited=[False]*self.vertex
       visited[u]=True
       queue.append(u)
       while queue:
          q_len=len(queue)
          if q_len:
             count=count+1
             if count==level:
                print(queue)
          while q_len:
              m=queue.pop(0)
              for i in self.graph[m]:
                 if not visited[i]:
                    queue.append(i)
                    visited[i]=True
              q_len=q_len-1

if __name__=="__main__":
   parser=argparse.ArgumentParser()
   parser.add_argument("--level1",help="Enter level1")
   parser.add_argument("--level2",help="Enter level2")
   parser.add_argument("--level3",help="Enter level3")
   parser.add_argument("--level4",help="Enter level4")
   args=parser.parse_args()
   level1=int(args.level1)
   level2=int(args.level2)
   level3=int(args.level3)
   level4=int(args.level4)
   graph=Graph(4)
   graph.add_edges(2,0)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   print("The queue contents at level1")
   graph.BFS(2,level1)
   print("The queue contents at level2")
   graph.BFS(2,level2)
   print("The queue contents at level3")
   graph.BFS(2,level3)
   print("The queue contents at level4")
   graph.BFS(2,level4)


   
   