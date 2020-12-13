import sys
INF=sys.maxsize
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=None
       self.next=None

   def setgraph(self,M):
       self.graph=M

   def setnext(self,N):
       self.next=N

   def reconstruct_path(self,start,end):
       path=[]
       if self.graph[start][end]==INF:
          return path
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
   graph=Graph(4)
   M=[[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
   graph.setgraph(M)
   N=[[j if M[i][j]!=INF else INF for j in range(graph.vertex)]for i in range(graph.vertex)]
   graph.setnext(N)
   graph.floyd_warshall()
   print(M)
   print(N)
   print(graph.reconstruct_path(0,3))


         