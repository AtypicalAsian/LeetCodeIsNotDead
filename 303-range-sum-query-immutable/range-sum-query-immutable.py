class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSumArr = []
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            self.prefixSumArr.append(currSum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSumArr[right]
        else:
            return self.prefixSumArr[right] - self.prefixSumArr[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)