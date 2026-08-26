class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Preform a dfs search on the graph
        #checking is there is a cycle
        #and then checking if the length of visited is
        #equal to n
        #make sure to go back to the parent

        #build an adgency graph
        adj_graph = defaultdict(list)
        for a,b in edges:
            adj_graph[a].append(b)
            adj_graph[b].append(a)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbors in adj_graph[node]:
                if not neighbors == prev and not dfs(neighbors, node):
                        return False
                        
            return True

        return dfs(0, None) and len(visited) == n