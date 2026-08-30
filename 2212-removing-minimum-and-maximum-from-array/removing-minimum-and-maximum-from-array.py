class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        minIdx, maxIdx = nums.index(min(nums)), nums.index(max(nums))

        l,r = min(minIdx,maxIdx), max(minIdx,maxIdx)
        first,last = r+1,n-l
        one_from_front_and_last = (n-r) + (l+1)
        return min(first,last,one_from_front_and_last)