class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for src,dst,dis in roads:
            g[src].append((dst,dis))
            g[dst].append((src,dis))
        res = float('inf')
        visited = set()
        queue = deque([1])

        while queue:
            curr = queue.popleft()
            for nb, dis in g[curr]:
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
                res=min(dis,res)
        return res