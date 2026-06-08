class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        leftArr = []
        rightArr = []
        pc = 0

        for i in range(0,n):
            if nums[i] == pivot:
                pc+=1
            elif nums[i] > pivot:
                rightArr.append(nums[i])
            else:
                leftArr.append(nums[i])
        res = leftArr + [pivot]*pc + rightArr
        return res