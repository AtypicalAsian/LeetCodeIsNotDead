class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        alphabet = [0] * 26
        for c in s:
            alphabet[ord(c) - ord('a')] += 1

        half_parts = []
        middle = ''
        for i in range(26):
            currCount = alphabet[i]
            char = chr(i + ord('a'))
            if currCount % 2 == 1:
                middle = char
            half_parts.append(char * (currCount//2))
        half = ''.join(half_parts)
        res = half + middle + half[::-1]
        return res