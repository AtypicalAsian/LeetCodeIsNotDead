class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self.digit_sum(n)
        return n==1
        
    
    def digit_sum(self,n):
        currSum = 0
        while n > 0:
            currSum += (n%10)**2
            n //= 10
        return currSum