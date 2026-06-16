class Solution:
    def processStr(self, s: str) -> str:
        res = []
        lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        # print(lowercase)
        for c in s:
            if c in lowercase:
                res.append(c)
            elif c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res.extend(res)
            elif c == "%":
                res.reverse()
            # print(res)

        return ''.join(res)