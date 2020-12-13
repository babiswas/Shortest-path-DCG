import sys
class Graph:
   def __init__(self,vertex):
       self.vertex=vertex
       self.graph=[]

   def display_parent(self,parent):
       for i in range(self.vertex):
          print(f"{parent[i]}---->{i} is {self.graph[parent[i]][i]}")


   def get_minm(self,weight,visited):
       minm=sys.maxsize
       minindex=0
       for i in range(self.vertex):
          if not visited[i] and weight[i]<minm:
             minm=weight[i]
             minindex=i
       return minindex

   def find_mst(self,src):
       weight=[sys.maxsize]*self.vertex
       visited=[False]*self.vertex
       parent=[-1]*self.vertex
       weight[src]=0
       for i in range(self.vertex):
          index=self.get_minm(weight,visited)
          visited[index]=True
          for j in range(self.vertex):
             if visited[j]==False and self.graph[index][j]>0 and weight[j]>self.graph[index][j]:
                weight[j]=self.graph[index][j]
                parent[j]=index
       self.display_parent(parent)

if __name__=="__main__":
   graph=Graph(5)
   graph.graph=[[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
   graph.find_mst(0)
  
   
     

          
          
          