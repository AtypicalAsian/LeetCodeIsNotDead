class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,val in enumerate(temperatures):
            # curr > top stk -> pop entire stack
            if stack and val > stack[-1][1]:
                while stack and val > stack[-1][1]:
                    currTempIndex, _ = stack.pop()
                    res[currTempIndex] = i - currTempIndex
                stack.append((i,val))
            else:
                stack.append((i,val))
        return res
                    
