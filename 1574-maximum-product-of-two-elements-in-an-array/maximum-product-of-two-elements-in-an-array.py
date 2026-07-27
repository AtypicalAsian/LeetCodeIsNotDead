class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest, second_biggest = 0,0
        maxProd = -float('inf')
        for i in range(len(nums)):
            if nums[i] > biggest:
                second_biggest = biggest
                biggest = nums[i]
            elif second_biggest < nums[i] <= biggest:
                second_biggest = nums[i]
        # print(biggest, second_biggest)
        return (biggest-1) * (second_biggest-1)

                
            
