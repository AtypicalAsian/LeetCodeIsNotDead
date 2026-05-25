class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rows,cols = len(s1),len(s2)
        if (rows + cols) != len(s3):
            return False
        dp = [[False]*(cols+1) for _ in range(rows+1)]
        dp[0][0] = True

        # Fill first row
        for i in range(1,rows+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # Fill first col
        for j in range(1,cols+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # Fill dp table
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        
        return dp[rows][cols]