class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSumMap = defaultdict(int)
        prefixSumMap[0] = 1
        currSum, count = 0,0
        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - goal
            if diff in prefixSumMap:
                count += prefixSumMap[diff]
            prefixSumMap[currSum] += 1
        return count