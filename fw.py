import sys
INF=sys.maxsize
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=None
   def input_matrix(self,M):
        self.graph=M
   def display(self):
       print(M)
   def APSP(self):
     for k in range(self.vertex):
      for i in range(self.vertex):
           for j in range(self.vertex):
               if self.graph[i][j]>self.graph[i][k]+self.graph[k][j]:
                   self.graph[i][j]=self.graph[i][k]+self.graph[k][j]

if __name__=="__main__":
   M=[[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
   graph=Graph(4)
   graph.input_matrix(M)
   graph.APSP()
   graph.display()

   
   
   
       
    
   