from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)

   def add_edges(self,u,v):
       self.graph[u].append(v)

   def connect_edge(self,l):
       stack=self.topsort()
       stack=stack[::-1]
       for i in l:
          if stack.index(i[0])<stack.index(i[1]):
             pass
          else:
             m=(i[1],i[0])
             l.remove(i)
             l.append(m)
       print(l)

   def topsort_util(self,u,visited,stack):
        visited[u]=True
        for i in self.graph[u]:
           if not visited[i]:
              self.topsort_util(i,visited,stack)
        stack.append(u)

   def topsort(self):
      stack=[]
      visited=[False]*self.vertex
      for i in range(self.vertex):
        if not visited[i]:
           self.topsort_util(i,visited,stack)
      return stack

if __name__=="__main__":
   graph=Graph(6)
   graph.add_edges(1,2)
   graph.add_edges(1,4)
   graph.add_edges(1,3)
   graph.add_edges(2,3)
   graph.add_edges(2,4)
   graph.add_edges(3,4)
   graph.add_edges(0,1)
   graph.add_edges(0,5)
   graph.add_edges(5,2)
   graph.add_edges(5,1)
   print("Connecting Edges")
   graph.connect_edge([(0,3),(0,2),(5,4)])
   
   

   