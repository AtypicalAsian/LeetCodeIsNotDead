class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            currDistance = self.get_distance(point[0],point[1])
            heapq.heappush(max_heap,(-currDistance,[point[0],point[1]]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [p for _,p in max_heap]

    def get_distance(self,x1,y1):
        return x1**2 + y1**2