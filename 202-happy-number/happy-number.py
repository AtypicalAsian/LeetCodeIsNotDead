class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        while (n != 1) and (n not in seen_nums):
            seen_nums.add(n)
            n = self.getSquaredDigitSum(n)
        return n == 1
    
    def getSquaredDigitSum(self,n):
        currSum = 0
        while n > 0:
            digit = n % 10
            currSum += digit ** 2
            n //= 10
        return currSum