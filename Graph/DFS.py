class Graph:
    def __init__(self,vno):
        self.vertex_count = vno 
        self.adj_list = { v:[] for v in range(vno) }
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))

    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("V",vertex,":",n)
    
    def DFS(self,s):
        #Mark all vertices as not visited
        visited = [False] * self.vertex_count
        self.dfs_recursive(s,visited)
        print()
    def dfs_recursive(self,v,visited):
        # Mark the current vertex as visited
        visited[v]=True
        print(v,end=" ")
        for neighbor,_ in self.adj_list[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor,visited)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_adj_list()
print("DFS starting from vertex 0:")
g.DFS(0)
