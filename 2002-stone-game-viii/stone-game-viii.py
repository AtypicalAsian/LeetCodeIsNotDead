class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        def dfs(i):
            nonlocal n, pref
            if i == n-2:
                return pref[i+1]
            
            if i in memo:
                return memo[i]
            skip = dfs(i+1)
            pick = pref[i+1] - dfs(i+1)
            memo[i] = max(pick,skip)

            return memo[i]
        n = len(stones)
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1,n):
            pref[i] = pref[i-1] + stones[i]
        memo = dict()
        return dfs(0)