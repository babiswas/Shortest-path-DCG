from collections import defaultdict

class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=defaultdict(list)
   def add_edge(self,u,v):
       self.graph[u].append(v)
   def util(self,u,visited):
       visited[u]=True
       for i in self.graph[u]:
          if not visited[i]:
             self.util(i,visited)
   def mother_vertex(self):
       mother=0
       visited=[False]*self.vertex
       for i in range(self.vertex):
          if not visited[i]:
            self.util(i,visited)
            mother=i
       visited=[False]*self.vertex
       self.util(mother,visited)
       if False not in visited:
          print(f"{mother} is the mother vertex")
       else:
          print("Mother vertex do not exist")

if __name__=="__main__":
   graph=Graph(4)
   graph.add_edge(0,2)
   graph.add_edge(2,0)
   graph.add_edge(1,2)
   graph.add_edge(0,1)
   graph.add_edge(2,3)
   graph.add_edge(3,3)
   graph.mother_vertex()

   
            