class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        ## two smallest negative integers and largest positive integer
        candidateA = nums[0] * nums[1] * nums[-1]

        ## three largest positive integers
        candidateB = nums[-1] * nums[-2] * nums[-3]

        return max(candidateA, candidateB)
        