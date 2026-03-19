class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        tracker = [0] * 101
        for person in logs:
            tracker[person[0]-1950] += 1
            tracker[person[1]-1950] -= 1
        
        currSum = 0
        maxPop = 0
        earliest = 0
        for i in range(101):
            currSum += tracker[i]
            if currSum > maxPop:
                maxPop = currSum
                earliest = i + 1950
        return earliest