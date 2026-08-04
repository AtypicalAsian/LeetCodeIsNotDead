class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        minNum = min(nums)
        maxNum = max(nums)

        for num in range(minNum, maxNum+1):
            if num not in nums:
                ans.append(num)
        
        return ans