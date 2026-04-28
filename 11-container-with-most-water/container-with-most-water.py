class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxArea = 0
        while left <= right:
            currArea = self.getArea(height[left],height[right],left,right)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(currArea,maxArea)
        return maxArea
            

    def getArea(self,h1,h2,i1,i2):
        return min(h1,h2) * (i2-i1)