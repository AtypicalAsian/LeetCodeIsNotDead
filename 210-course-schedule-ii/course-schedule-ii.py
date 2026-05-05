class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                currNode = queue.popleft()
                res.append(currNode)
                for nxt in graph[currNode]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
        if len(res) == numCourses:
            return res
        return []