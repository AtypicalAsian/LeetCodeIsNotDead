class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum, maxNum = float('inf'), -1
        for num in nums:
            minNum = min(minNum,num)
            maxNum = max(maxNum,num)
        
        return self.getGCD(minNum, maxNum)
    
    def getGCD(self, smallNum, largeNum):
        while largeNum:
            smallNum, largeNum = largeNum, smallNum % largeNum
        return abs(smallNum)