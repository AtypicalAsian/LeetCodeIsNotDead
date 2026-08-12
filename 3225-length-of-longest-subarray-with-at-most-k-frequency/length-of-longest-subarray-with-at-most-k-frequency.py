class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqMap = defaultdict(int) #num : freq
        ans = 0
        left = 0

        # expand window right
        for right in range(len(nums)):
            freqMap[nums[right]] += 1
            while freqMap[nums[right]] > k:
                #shrink window from left
                freqMap[nums[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans
