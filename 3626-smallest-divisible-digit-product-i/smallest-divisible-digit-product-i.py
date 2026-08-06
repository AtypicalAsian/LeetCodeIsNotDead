class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n,n+11):
            currProd = self.digit_product(num)
            print(currProd)
            
            if (currProd % t) == 0:
                return num
        return -1
    
    def digit_product(self, num):
        prod = 1
        while num > 0:
            digit = num % 10
            prod *= digit
            num = num // 10
        return prod