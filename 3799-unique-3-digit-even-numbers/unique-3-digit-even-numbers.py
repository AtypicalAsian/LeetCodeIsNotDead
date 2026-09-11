from itertools import permutations

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # digits.length < 10 -> enumerate all, then filter out invalid ones
        n = len(digits)
        enumeration = []
        for indices in permutations(range(n),3):
            combo = [digits[i] for i in indices]
            enumeration.append(combo)
        res = set()

        for combo in enumeration:
            if (combo[0] == 0) or (combo[2] % 2 != 0):
                continue
            else:
                num = 0
                for d in combo:
                    num = num * 10 + d
                res.add(num)
        return len(res)
        
        