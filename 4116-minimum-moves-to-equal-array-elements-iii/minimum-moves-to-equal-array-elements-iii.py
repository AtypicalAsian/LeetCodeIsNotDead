class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        totalMoves = 0
        for num in nums:
            totalMoves += (target-num)
        return totalMoves