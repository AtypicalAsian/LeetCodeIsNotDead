class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        #initialize heap
        for i in range(len(points)):
            heapq.heappush(heap,(self.distance(points[i]),i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[j] for _,j in heap]

    def distance(self, point: List[int]) -> int:
        return (point[0] ** 2 + point[1] ** 2) * -1