class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for currI, currH in enumerate(heights):
            startI = currI
            while stack and currH < stack[-1][1]:
                prev = stack.pop()
                prevI = prev[0]
                prevH = prev[1]

                prevArea = (currI - prevI) * prevH
                maxArea = max(maxArea, prevArea)

                startI = prevI

            stack.append([startI, currH])

        while stack:
            prev = stack.pop()
            i = prev[0]
            h = prev[1]
            prevArea = (len(heights) - i) * h
            maxArea = max(maxArea, prevArea)
        return maxArea


test1 = Solution
print(test1.largestRectangleArea(None, [2, 1, 5, 6, 2, 3]))
