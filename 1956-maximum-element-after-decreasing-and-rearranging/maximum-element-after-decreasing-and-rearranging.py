class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxVal = 1
        for i in range(1,len(arr)):
            if arr[i] > maxVal:
                maxVal+=1
        return maxVal