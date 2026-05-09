class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start,res_end = 0,0
        for i in range(len(s)-1):
            oddLength = self.isPalindrome(s,i,i)
            if (oddLength[1]-oddLength[0]) > (res_end-res_start):
                res_start, res_end = oddLength[0], oddLength[1]
            
            evenLength = self.isPalindrome(s,i,i+1)
            if (evenLength[1]-evenLength[0]) > (res_end-res_start):
                res_start, res_end = evenLength[0], evenLength[1]
        return s[res_start:res_end+1]


    def isPalindrome(self,s,i,j):
        res = [0,0]
        while i>= 0 and j < len(s) and s[i] == s[j]:
            res = [i,j]
            i -= 1
            j += 1
        return res