class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = 10000000
        for i in range(len(arr)-1):
            minDiff = min(minDiff, abs(arr[i+1] - arr[i]))
        res = []
        for i in range(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            if diff == minDiff:
                res.append([arr[i],arr[i+1]])
        return res


        