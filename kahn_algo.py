from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edges(self,u,v):
       self.graph[u].append(v)
   def kahn_algo(self):
      count=0
      inner=[0]*self.vertex
      for i in range(self.vertex):
         for j in self.graph[i]:
            inner[j]=inner[j]+1
      queue=[]
      for i in range(self.vertex):
         if inner[i]==0:
            queue.append(i)
      while queue:
         m=queue.pop(0)
         print(m)
         for i in self.graph[m]:
            inner[i]=inner[i]-1
            if inner[i]==0:
               queue.append(i)
         count=count+1
      if count==self.vertex:
         print("Topsort is possible")
      else:
         print("There is a cycle in the graph")

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   graph.add_edges(3,1)
   graph.add_edges(4,1)
   graph.kahn_algo()
   print("Creating another graph")
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(2,0)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   graph.add_edges(3,3)
   graph.kahn_algo()
