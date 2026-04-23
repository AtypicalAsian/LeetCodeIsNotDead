class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLen,  left = 0,0
        zero_lim = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_lim -= 1
                while zero_lim < 0:
                    if nums[left] == 0:
                        zero_lim += 1
                    left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen - 1