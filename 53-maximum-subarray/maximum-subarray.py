class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Bottom up
        maxSum = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i],dp[i-1]+nums[i])    #start fresh or extend current subarray
            maxSum = max(maxSum,dp[i])
        return maxSum