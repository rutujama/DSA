class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
          self.adj_list[u].append((v,weight))    
          self.adj_list[v].append((u,weight))
        else:
            print("invalid entry")
    def remove_edge(self,u,v,weight):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(v,weight) for vertex,weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v]=[(u,weight) for vertex,weight in self.adj_list[v] if vertex!=u]
        else:
            print("invalid entry")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex,x in self.vertex_count[u] )
        else:
            print("invalid entry")
            return False
    def print_adj_list(self):
        for vertex ,n in self.adj_list.items():
            print("v",vertex,":",n)
g=Graph(5)
g.add_edge(4,1)
g.add_edge(3,1)                         
g.add_edge(2,3)                         
g.add_edge(2,1)        
g.add_edge(0,1) 
g.print_adj_list()       
        
        
      
      