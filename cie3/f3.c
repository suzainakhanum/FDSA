    
Algorithm Dfs(v)
//initially visited is set to zero
{
    visited[v]=1
    for all vertices w adjacent to u do
    {
        if(visited[w]==0)
        Dfs(w)
    }
}
g= Graph
g.add_edges(0,1)
g.add_edges(2,1)
g.add_edges(2,3)
