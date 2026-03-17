class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remMap = defaultdict(int)
        remMap[0] = -1
        currSum = 0
        for i,val in enumerate(nums):
            currSum += val
            rem = currSum % k
            if rem in remMap:
                if i - remMap[rem] >= 2:
                    return True
            else:
                remMap[rem] = i
        return False