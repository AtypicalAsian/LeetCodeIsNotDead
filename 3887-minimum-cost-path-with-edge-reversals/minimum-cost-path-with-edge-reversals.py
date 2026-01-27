import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list = [[] for _ in range(n)]
        rev_adj_list = [[] for _ in range(n)]

        for u, v, w in edges:
            adj_list[u].append((v, w))
            rev_adj_list[v].append((u, 2 * w))
        
        distance = [float("inf")] * n
        distance[0] = 0

        min_heap = []
        heapq.heappush(min_heap, (0, 0))

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            for ngbr, ngbr_dist in adj_list[node]:
                if dist + ngbr_dist < distance[ngbr]:
                    distance[ngbr] = dist + ngbr_dist
                    heapq.heappush(min_heap, (distance[ngbr], ngbr))
            

            for ngbr, ngbr_dist in rev_adj_list[node]:
                if dist + ngbr_dist < distance[ngbr]:
                    distance[ngbr] = dist + ngbr_dist
                    heapq.heappush(min_heap, (distance[ngbr], ngbr))

        if distance[-1] == float("inf"):
            return -1
        else:
            return distance[-1]