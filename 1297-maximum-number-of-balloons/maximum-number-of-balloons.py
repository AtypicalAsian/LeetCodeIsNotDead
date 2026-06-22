class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        ans = inf
        mp = defaultdict(int)
        for ch in text:
            if ch in target:
                mp[ch] += 1
        
        if len(mp) < 5: return 0
        for k, v in mp.items():
            if k in ["l", "o"]:
                ans = min(ans, v // 2)
            else:
                ans = min(ans, v)
        return ans