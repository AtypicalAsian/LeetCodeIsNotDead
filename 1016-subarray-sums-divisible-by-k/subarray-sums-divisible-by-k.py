class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # If a and b give same remainder % k --> (a-b) % k = 0
        count, currSum = 0,0
        prefixSumRemainderMap = defaultdict(int)
        prefixSumRemainderMap[0] = 1

        for num in nums:
            currSum += num
            remainder = currSum % k
            if remainder in prefixSumRemainderMap:
                count += prefixSumRemainderMap[remainder]
            prefixSumRemainderMap[remainder] += 1
        return count
        