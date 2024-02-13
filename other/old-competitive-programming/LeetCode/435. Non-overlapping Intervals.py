class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        numIntervalsRemoved = 0

        previousFinish = intervals[0][1]
        i = 1
        while (i < len(intervals)):
            start = intervals[i][0]
            finish = intervals[i][1]

            if (start < previousFinish):
                # there is overlap
                previousFinish = min(previousFinish, finish)
                numIntervalsRemoved += 1

            else:
                previousFinish = finish

            i += 1

        return numIntervalsRemoved
