class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd, even = True, True
        for num in sorted(nums1):
            odd = odd and num % 2 == 1
            even = even and num % 2 == 0
            if not odd and not even:
                return False
            if num % 2 == 1:
                return True
        return odd or even