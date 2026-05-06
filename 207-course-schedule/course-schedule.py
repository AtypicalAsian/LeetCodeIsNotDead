class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        
        # Run BFS/Topo Sort on Graph
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                count += 1
                currNode = queue.popleft()
                for nb in graph[currNode]:
                    indegree[nb] -= 1
                    if indegree[nb] == 0:
                        queue.append(nb)
        return count == numCourses
                