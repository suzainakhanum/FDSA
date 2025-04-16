class Graph:
    def __init__(self, vertices):
        self.adj_list = {}
    
    def add_edges(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u]=[]
        if v not in self.adj_list:
            self.adj_list[v]=[]
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", "->".join(map(str,self.adj_list[vertex])))
        print()
    def dfs(self, start_vertex):    
        visited = set()
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")
                stack.extend(neighbor for neighbor in self.adj_list[vertex] if neighbor not in visited)
        print()
   
g= Graph(5)
g.add_edges(0,1)
g.add_edges(0,2)
g.add_edges(1,3)
g.add_edges(1,4)
g.add_edges(2,4)
g.print_graph()
g.dfs(0)
g.dfs(1)
g.dfs(2)
g.dfs(3)
g.dfs(4)
