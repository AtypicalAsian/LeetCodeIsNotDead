class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, currCount = 0,0
        for num in nums:
            if num == 1:
                currCount += 1
            else:
                currCount = 0
            maxCount = max(maxCount, currCount)
        return maxCount