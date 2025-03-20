
class TimeMap:
    def __init__(self):
        self.map: dict[str, list[tuple(str, int)]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        l, r = 0, len(values) - 1
        while l < r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        if values[r][1] <= timestamp:
            return values[r][0]
        elif r > 0:
            return values[r - 1][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

o = TimeMap()
o.set("love", "high", 10)
o.set("love", "low", 20)
print(o.get("love", 5))
