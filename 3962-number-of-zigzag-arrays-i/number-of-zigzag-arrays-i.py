class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        dp = [1] * m
        for _ in range(n - 1):
            new_dp = [0] * m
            current_sum = 0
            for i in range(m):
                new_dp[i] = current_sum
                current_sum = (current_sum + dp[m - 1 - i]) % MOD
            dp = new_dp
        total = sum(dp) % MOD
        return (total * 2) % MOD