class Graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.graph=[]

    def add_edge(self,u,v):
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

    def iscyclic(self):
        parent=[-1]*self.vertex
        for i in self.graph:
            s1=self.find(i[0],parent)
            s2=self.find(i[1],parent)
            if s1==s2:
               return True
            self.union(s1,s2,parent)
        
        
if __name__=="__main__":
   graph=Graph(4)
   graph.add_edge(0,2)
   graph.add_edge(2,0)
   graph.add_edge(0,1)
   graph.add_edge(1,2)
   graph.add_edge(2,3)
   graph.add_edge(3,3)
   print(graph.iscyclic())
