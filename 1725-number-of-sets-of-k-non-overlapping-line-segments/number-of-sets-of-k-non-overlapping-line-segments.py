import math
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        N = n + k - 1
        r = 2*k
        return math.factorial(N) // (math.factorial(r) * math.factorial(N-r)) % 1000000007
