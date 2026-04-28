class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right = len(numbers)-1
        currSum = 0
        while left <= right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left+1,right+1]
            elif currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
        return [-1,-1]