class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currSum = 0
        prefixRemMap = defaultdict(int)

        for i,val in enumerate(nums):
            currSum += val
            currRem = currSum % k
            if (currRem == 0) and (i >= 1):
                return True
            elif currRem in prefixRemMap:
                if (i - prefixRemMap[currRem]) > 1:
                    return True
            else:
                prefixRemMap[currRem] = i
        return False
        