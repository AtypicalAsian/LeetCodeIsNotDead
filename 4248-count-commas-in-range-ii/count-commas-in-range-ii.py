class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        if n < 1000:
            return 0
        
        lb = 1000
        ub = 999999
        c = 1
        
        while True:
            if n >= lb:
                if n > ub:
                    ans += (ub - lb + 1) * c
                else:
                    ans += (n - lb + 1) * c
                    break
                
                c += 1
                lb = lb * 1000
                ub = ub * 1000 + 999
        
        return ans