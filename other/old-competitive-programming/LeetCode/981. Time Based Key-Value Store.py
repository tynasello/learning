class TimeMap:

    def __init__(self):
        self.store = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store.get(key)
        lenValues = len(values)
        left = 0
        right = lenValues - 1

        # BS
        while left <= right:
            middle = left + (right - left) // 2
            if values[middle][0] == timestamp:
                return values[left][1]

            if values[middle][0] > timestamp:
                right = middle - 1
            else:
                left = middle + 1

        return values[right][1] if values[right][0] <= timestamp else ""


'''
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

{'foo': [[1, 'bar'], [4, 'bar2']]}
lenValues = 2
left = 0
right = 1
'''
