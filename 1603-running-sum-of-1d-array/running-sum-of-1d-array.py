class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        runningSum = [currSum := currSum + x for x in nums]
        return runningSum
