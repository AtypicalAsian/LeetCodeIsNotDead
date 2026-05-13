class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums) # 4 -> 2
        res, cur = N, N
        ranges = [0] * (2 * limit + 2)
        for i in range(N // 2):
            a, b = nums[i], nums[N - i - 1]
            s, e = min(a, b), max(a, b)

            ranges[s + 1] -= 1
            ranges[s + e] -= 1
            ranges[s + e + 1] += 1
            ranges[e + limit + 1] += 1

        for i in range(2, 2 * limit + 1):
            cur += ranges[i]
            res = min(res, cur)
            
        return res