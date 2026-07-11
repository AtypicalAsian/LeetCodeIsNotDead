class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        #Create graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        #DFS to explore each component + count number of nodes and edges
        def dfs(node,visited):
            visited[node] = True
            vertex_count, edge_count = 1, len(graph[node])
            for nb in graph[node]:
                if not visited[nb]:
                    more_vertx, more_edges = dfs(nb,visited)
                    vertex_count += more_vertx
                    edge_count += more_edges
            return vertex_count, edge_count

        count = 0
        for node in range(n):
            if not visited[node]:
                v_count, e_count = dfs(node,visited)
                #if vertex * (vertex-1) == edge count -> exist edge between every pair of nodes
                if (v_count * (v_count-1)) == e_count:
                    count += 1
        return count
        