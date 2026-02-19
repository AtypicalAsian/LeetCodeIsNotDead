class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #~subarray sum divisible by k, but added constraint size>=2
        currSum = 0
        prefixSumRemainderMap = defaultdict(int)
        prefixSumRemainderMap[0] = -1

        for i,val in enumerate(nums):
            currSum += val
            remainder = currSum % k
            if remainder in prefixSumRemainderMap:
                if (i-prefixSumRemainderMap[remainder]) >= 2:
                    return True
            else: #Only update when encounter new remainder --> want to maximize length of subarray
                prefixSumRemainderMap[remainder] = i
        return False



        