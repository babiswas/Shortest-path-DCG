class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v,w):
       self.graph.append([u,v,w])

   def display(self,dist,src):
      for i in range(self.vertex):
          print(f"{src}-->{i}={dist[i]}")

   def bellman_ford(self,src):
       dist=[float("inf")]*self.vertex
       dist[src]=0
       for i in range(self.vertex-1):
          for u,v,w in self.graph:
             if dist[u]!=float("inf") and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
       self.display(dist,src)
       for u,v,w in self.graph:
          if dist[v]>dist[u]+w:
             print("There is a cycle in the graph from u to v")
       print("After the extra cycle")
       self.display(dist,src)

if  __name__=="__main__":
    graph=Graph(5)
    graph.add_edges(0,1,-1)
    graph.add_edges(0,2,4)
    graph.add_edges(1,2,3)
    graph.add_edges(1,3,2)
    graph.add_edges(1,4,2)
    graph.add_edges(3,2,5)
    graph.add_edges(3,1,1)
    graph.add_edges(4,3,-3)
    graph.bellman_ford(0)

    