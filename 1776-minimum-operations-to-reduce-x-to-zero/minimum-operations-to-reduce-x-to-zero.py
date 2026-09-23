class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        mp = {0: 0}
        prefix = 0
        for i, num in enumerate(nums, 1): 
            prefix += num
            mp[prefix] = i 
            
        ans = mp.get(x, inf)
        for i, num in enumerate(reversed(nums), 1): 
            x -= num
            if x in mp and mp[x] + i <= len(nums): ans = min(ans, i + mp[x])
        return ans if ans < inf else -1 