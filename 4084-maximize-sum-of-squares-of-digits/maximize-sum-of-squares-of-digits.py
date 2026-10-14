class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=""
        for i in range(9,0,-1):
            d,r=divmod(sum,i)
            if(d>0):
                res+=str(i)*d
                sum=r
        if(len(res)<num):
            res+="0"*(num-len(res))
        return res if len(res)==num else ""