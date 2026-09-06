class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n+1):
                dp[i+1][j] = dp[i][j]
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] += dp[i][j]
        return dp[m][n]
    
