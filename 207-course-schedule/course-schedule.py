class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Construct graph (adj list)
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        
        # Run BFS on graph to find ordering

        # Init queue with nodes where indegree = 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                currNode = queue.popleft()
                count += 1
                for nxt in graph[currNode]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
        return count == numCourses
