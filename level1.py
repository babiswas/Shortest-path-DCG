from collections import defaultdict
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edge(self,u,v):
       self.graph[u].append(v)
   def BFS(self,u,level):
      count=0
      queue=[]
      visited=[False]*self.vertex
      queue.append(u)
      visited[u]=True
      while queue:
         m=len(queue)
         if m!=0:
           count=count+1
           if count==level:
              print(queue)
              break
         while m:
            n=queue.pop(0)
            for i in self.graph[n]:
               if not visited[i]:
                  queue.append(i)
                  visited[i]=True
            m=m-1

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edge(0,2)
   graph.add_edge(2,0)
   graph.add_edge(1,2)
   graph.add_edge(0,1)
   graph.add_edge(2,3)
   graph.add_edge(3,3)
   for i in range(4):
     graph.BFS(2,i)

 