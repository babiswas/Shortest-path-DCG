import sys

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=None
       self.edge=[]

   def display(self,parent):
       for i in range(self.vertex):
          print(f"{parent[i]}----->{i}={self.graph[parent[i]][i]}")

   def setgraph(self):
       M=[[0 for i in range(self.vertex)]for j in range(self.vertex)]
       for i in self.edge:
          M[i[0]][i[1]]=i[2]
       self.graph=M

   def add_edge(self,u,v,w):
       self.edge.append((u,v,w))

   def find_mst(self,src):
       key=[sys.maxsize]*self.vertex
       key[src]=0
       visited=[False]*self.vertex
       parent=[-1]*self.vertex
       for j in range(self.vertex):
          index=self.minm_key(key,visited)
          visited[index]=True
          for i in range(self.vertex):
            if visited[i]==False and self.graph[index][i]>0 and key[i]>self.graph[index][i]:
               key[i]=self.graph[index][i]
               parent[i]=index
       self.display(parent)

   def minm_key(self,key,visited):
       minm=sys.maxsize
       minindex=0
       for i in range(self.vertex):
         if key[i]<minm and visited[i]==False:
            minm=key[i]
            minindex=i
       return minindex

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edge(0,1,4)
   graph.add_edge(0,7,8)
   graph.add_edge(1,7,11)
   graph.add_edge(1,2,8)
   graph.add_edge(7,6,1)
   graph.add_edge(7,8,7)
   graph.add_edge(8,6,6)
   graph.add_edge(2,8,2)
   graph.add_edge(6,5,2)
   graph.add_edge(2,5,4)
   graph.add_edge(2,3,7)
   graph.add_edge(3,5,14)
   graph.add_edge(3,4,9)
   graph.add_edge(5,4,10)
   graph.setgraph()
   print(graph.graph)
   graph.find_mst(0)
   

