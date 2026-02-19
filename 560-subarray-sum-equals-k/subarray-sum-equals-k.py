class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefixSumMap = defaultdict(int)
        prefixSumMap[0] = 1
        count = 0

        for num in nums:
            currSum += num
            seenPrefixSum = currSum - k
            if seenPrefixSum in prefixSumMap:
                count += prefixSumMap[seenPrefixSum]
            prefixSumMap[currSum] += 1
        return count