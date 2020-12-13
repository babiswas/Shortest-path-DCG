class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]
   def add_edges(self,u,v):
      self.graph.append((u,v))
   def find(self,u,arr):
      while arr[u]!=-1:
          u=arr[u]
      return u
   def union(self,u,v,arr):
      s1=self.find(u,arr)
      s2=self.find(v,arr)
      if s1!=s2:
         arr[u]=v
   def iscyclic(self):
      arr=[-1]*self.vertex
      for i in self.graph:
         s1=self.find(i[0],arr)
         s2=self.find(i[1],arr)
         if s1!=s2:
            self.union(s1,s2,arr)
         else:
            return True
      return False

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edges(0,2)
   graph.add_edges(0,1)
   graph.add_edges(1,2)
   graph.add_edges(2,3)
   print(graph.iscyclic())

   