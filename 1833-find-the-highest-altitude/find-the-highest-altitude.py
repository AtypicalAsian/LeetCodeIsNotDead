class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        curr = 0
        for alt in gain:
            curr += alt
            maxAlt = max(maxAlt,curr)
        return maxAlt