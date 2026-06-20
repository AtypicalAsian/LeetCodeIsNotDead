class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        restrictions.sort()
        m = len(restrictions)

        if m == 0:
            return n - 1

        has_last = restrictions[-1][0] == n
        size = m + 1 + (0 if has_last else 1)
        arr = [[0, 0] for _ in range(size)]
        arr[0] = [1, 0]

        for i in range(m):
            pos, limit = restrictions[i]
            dist = pos - arr[i][0]
            allowed = arr[i][1] + dist
            arr[i + 1] = [pos, min(limit, allowed)]

        if not has_last:
            dist = n - arr[m][0]
            arr[m + 1] = [n, min(n - 1, arr[m][1] + dist)]

        for i in range(size - 2, -1, -1):
            dist = arr[i + 1][0] - arr[i][0]
            arr[i][1] = min(arr[i][1], arr[i + 1][1] + dist)

        ans = 0

        for i in range(1, size):
            left_pos, h1 = arr[i - 1]
            right_pos, h2 = arr[i]

            peak = (right_pos - left_pos - abs(h1 - h2)) // 2 + max(h1, h2)
            ans = max(ans, peak)
        return ans