class Subset:
   def __init__(self,parent,rank):
       self.parent=parent
       self.rank=rank

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def find_mst(self):
       edge=[]
       def getitem(m):
          return m[2]
       parent=[]
       for i in range(self.vertex):
          parent.append(Subset(i,0))
       self.graph=sorted(self.graph,key=getitem)
       for i in self.graph:
          s1=self.find(i[0],parent)
          s2=self.find(i[1],parent)
          if s1!=s2:
             edge.append(i)
             self.union(s1,s2,parent)
       print(edge)
     

   def add_edge(self,u,v,w):
       self.graph.append((u,v,w))

   def union(self,u,v,parent):
       s1=self.find(u,parent)
       s2=self.find(v,parent)
       if s1!=s2:
          if parent[s1].rank>parent[s2].rank:
             parent[s2].parent=s1
             parent[s1].rank=parent[s1].rank+1
          elif parent[s2].rank>parent[s1].rank:
             parent[s1].parent=s2
             parent[s2].rank=parent[s2].rank+1
          else:
             parent[s1].parent=s2
             parent[s2].rank=parent[s2].rank+1
          
   def find(self,u,parent):
       while parent[u].parent!=u:
           u=parent[u].parent
       return u

if __name__=="__main__":
   graph=Graph(9)
   graph.add_edge(0,7,8)
   graph.add_edge(0,1,4)
   graph.add_edge(1,7,11)
   graph.add_edge(7,6,1)
   graph.add_edge(7,8,7)
   graph.add_edge(8,6,6)
   graph.add_edge(1,2,8)
   graph.add_edge(2,8,2)
   graph.add_edge(6,5,2)
   graph.add_edge(2,5,4)
   graph.add_edge(2,3,7)
   graph.add_edge(3,5,14)
   graph.add_edge(3,4,9)
   graph.add_edge(5,4,10)
   graph.find_mst()



   
       