class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        directions = [[0, 1], [1, 0]]
        R, C = len(grid), len(grid[0])
        
        @cache
        def backtrack(r, c, st):
            if grid[r][c] == ')':
                st -= 1
            else:
                st += 1

            if st < 0:
                return False

            if r == R-1 and c == C-1:
                return st == 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < R and nc < C):
                    if backtrack(nr, nc, st):
                        return True
            
            return False

        return backtrack(0, 0, 0)