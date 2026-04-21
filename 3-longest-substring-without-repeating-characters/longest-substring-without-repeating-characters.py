class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        charFreqMap = {}
        for i in range(len(s)):
            if s[i] in charFreqMap:
                #prevent left pointer from going backwards
                left = max(left,charFreqMap[s[i]] + 1)
                charFreqMap[s[i]] = i
            else:
                charFreqMap[s[i]] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen