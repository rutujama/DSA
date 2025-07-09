class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_matrix=[[0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[u][v]=weight 
        else:
            print("invalid value")
    def delete_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[u][v]=0 
        else:
            print("invalid value")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("invalid value")
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
          print(" ".join(map(str,row_list)))
g=Graph(5)
g.add_edge(1,4)  
g.add_edge(3,4)  
g.add_edge(2,4)  
g.add_edge(3,2)  
g.add_edge(1,1)  
g.print_adj_matrix()                
        
                
                      