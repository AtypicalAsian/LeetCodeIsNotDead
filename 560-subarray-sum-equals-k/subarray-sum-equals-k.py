class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum, count = 0,0
        prefixMap = defaultdict(int)
        prefixMap[0] = 1
        for i,val in enumerate(nums):
            currSum += nums[i]
            seenPrefixSum = currSum - k
            if seenPrefixSum in prefixMap:
                count += prefixMap[seenPrefixSum]
            prefixMap[currSum] += 1
        return count
