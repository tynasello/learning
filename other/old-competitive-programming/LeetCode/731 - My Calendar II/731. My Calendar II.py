class MyCalendarTwo:
    def __init__(self):
        self.singleBooked = []
        self.doubleBooked = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.doubleBooked:
            if start < e and end > s:
                return False

        for s, e in self.singleBooked:
            if start < e and end > s:
                doubleStart = max(s, start)
                doubleEnd = min(e, end)
                self.doubleBooked.append([doubleStart, doubleEnd])
        self.singleBooked.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
