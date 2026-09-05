class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxes, mins = [nums[0]], [nums[-1]]
        for i in range(1, len(nums)):
            maxes.append(max(maxes[-1], nums[i]))
            mins.append(min(mins[-1], nums[~i]))
        for i in range(len(maxes)):
            if maxes[i]-mins[~i] <= k:
                return i
        return -1