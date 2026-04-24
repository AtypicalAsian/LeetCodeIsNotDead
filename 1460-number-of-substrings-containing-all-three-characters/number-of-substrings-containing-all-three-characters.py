class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count,left = 0,0
        charCount = defaultdict(int)
        for right in range(len(s)):
            charCount[s[right]] += 1
            while len(charCount) == 3:
                count += len(s) - right
                charCount[s[left]] -= 1
                if charCount[s[left]] == 0:
                    del charCount[s[left]]
                left += 1
        return count
                