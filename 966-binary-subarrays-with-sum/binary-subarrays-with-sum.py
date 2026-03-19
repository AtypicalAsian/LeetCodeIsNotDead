class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atMostGoalCount(nums,goal) - self.atMostGoalCount(nums,goal-1)
    
    def atMostGoalCount(self,nums,goal):
        if goal < 0:
            return 0
        left = 0
        currSum, count = 0,0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum > goal:
                currSum -= nums[left]
                left += 1
            count += right - left + 1 # count of unique subarrays ending at right
        return count


            