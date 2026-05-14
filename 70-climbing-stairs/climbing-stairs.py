class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        ### Top Down
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
    
        