class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = -float('inf')
        left = 0
        while left < len(nums):
            for right in range(left+1,len(nums)):
                currProd = (nums[left]-1) * (nums[right]-1)
                maxProd = max(maxProd,currProd)
            left += 1
        return maxProd
            
