import sys
INF=sys.maxsize
class Graph:
  def __init__(self,vertex):
      self.vertex=vertex
      self.graph=None
      self.next=None

  def setgraph(self,M):
      self.graph=M

  def setnext(self):
     self.next=[[j if self.graph[i][j]!=INF else INF for j in range(self.vertex)]for i in range(self.vertex)]

  def getgraph(self):
     return self.graph

  def reconstruct_path(self,start,end):
      path=[]
      if self.graph[start][end]==INF:
         return None
      var=start
      while var!=end:
         if var==-1:
            return None
         path.append(var)
         var=self.next[var][end]
      if self.next[var][end]==-1:
         return None
      path.append(end)
      return path

  def floyd_warshall(self):
      for k in range(self.vertex):
         for i in range(self.vertex):
           for j in range(self.vertex):
              if self.graph[i][j]>self.graph[i][k]+self.graph[k][j]:
                 self.graph[i][j]=self.graph[i][k]+self.graph[k][j]
                 self.next[i][j]=self.next[i][k]

if __name__=="__main__":
   M=[[0,5,sys.maxsize,10],[sys.maxsize,0,3,sys.maxsize],[sys.maxsize,sys.maxsize,0,1],[sys.maxsize,sys.maxsize,sys.maxsize,0]]
   graph=Graph(4)
   graph.setgraph(M)
   graph.setnext()
   graph.floyd_warshall()
   print(graph.reconstruct_path(0,3))
   print(graph.getgraph())



   
