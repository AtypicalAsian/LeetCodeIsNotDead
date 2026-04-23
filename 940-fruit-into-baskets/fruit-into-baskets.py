class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        maxCount = 0
        typeCountMap = defaultdict(int)
        for i in range(len(fruits)):
            typeCountMap[fruits[i]] += 1
            while len(typeCountMap) > 2:
                typeCountMap[fruits[left]] -= 1
                if typeCountMap[fruits[left]] == 0:
                    del typeCountMap[fruits[left]]
                left += 1
            maxCount = max(maxCount, i - left + 1)
        return maxCount

        