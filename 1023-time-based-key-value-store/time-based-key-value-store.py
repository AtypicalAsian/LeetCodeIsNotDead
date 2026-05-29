class TimeMap:

    def __init__(self):
        self.kvStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvStore[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvStore:
            return ""
        l,r = 0,len(self.kvStore[key])-1
        entries = self.kvStore[key]

        res = ""
        while l <= r:
            mid = (l+r)//2
            if entries[mid][0] <= timestamp:
                l = mid + 1
                res = entries[mid][1]
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)