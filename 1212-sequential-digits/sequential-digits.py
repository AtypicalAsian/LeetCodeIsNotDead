class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = list()

        for window in range(floor(log10(low)) + 1, floor(log10(high)) + 2):
            for start in range(10 - window):
                num = 0
                for j in range(start,start+window):
                    num = num * 10 + j + 1
                if num > high:
                    return res
                if low <= num <= high:
                    res.append(num)
        
        return res