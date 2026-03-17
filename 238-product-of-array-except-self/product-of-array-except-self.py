class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefix = [1] * len(nums)
        rightSuffix = [1] * len(nums)
        currProd = 1

        for i in range(0,len(nums)-1):
            currProd *= nums[i]
            leftPrefix[i+1] *= currProd
        
        currProd = 1
        for i in range(len(nums)-1,0,-1):
            currProd *= nums[i]
            rightSuffix[i-1] *= currProd

        res = [1] * len(nums)
        for i in range(len(leftPrefix)):
            res[i] = rightSuffix[i] * leftPrefix[i]
        return res
