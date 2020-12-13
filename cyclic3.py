class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def add_edges(self,u,v):
       self.graph.append((u,v))

   def union(self,u,v,parent):
       s1=self.find(u,parent)
       s2=self.find(v,parent)
       if s1!=s2:
          parent[u]=v
       
   def find(self,u,parent):
       while parent[u]!=-1:
           u=parent[u]
       return u

   def is_cyclic(self):
       parent=[-1 for i in range(self.vertex)]
       for i in self.graph:
           s1=self.find(i[0],parent)
           s2=self.find(i[1],parent)
           if s1!=s2:
              self.union(s1,s2,parent)
           else:
              return True
       return False

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(5,0)
   graph.add_edges(4,0)
   graph.add_edges(4,1)
   graph.add_edges(5,2)
   graph.add_edges(2,3)
   print(graph.is_cyclic())
   print("Creating a new graph")
   graph1=Graph(6)
   graph1.add_edges(5,0)
   graph1.add_edges(4,0)
   graph1.add_edges(4,1)
   graph1.add_edges(5,2)
   graph1.add_edges(2,3)
   graph1.add_edges(3,1)
   print(graph1.is_cyclic())

   
   
   
