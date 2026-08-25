class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        for i in range(1,102):
            currMultiple = k * i
            if currMultiple not in numSet:
                return currMultiple
        return currMultiple