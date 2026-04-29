class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stk.append(s[i])
            else:
                if len(stk) == 0:
                    return False
                elif ((stk[-1] == '(' and s[i] == ')') or (stk[-1] == '{' and s[i] == '}') or (stk[-1] == '[' and s[i] == ']')):
                    stk.pop(-1)
                else:
                    return False
        if len(stk) == 0:
            return True
        return False