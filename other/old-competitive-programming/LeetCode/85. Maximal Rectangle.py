class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        maxArea = 0

        for rowIndex, row in enumerate(matrix):
            for elIndex, el in enumerate(row):

                el = int(el)

                if el == 1 and rowIndex != 0:
                    matrix[rowIndex][elIndex] = int(matrix[rowIndex - 1][elIndex]) + 1

                stack = []
                currArea = 0

            for currI, currH in enumerate(matrix[rowIndex]):
                currH = int(currH)
                startI = currI
                while stack and currH < stack[-1][1]:
                    prev = stack.pop()
                    prevI = prev[0]
                    prevH = prev[1]

                    prevArea = (currI - prevI) * prevH
                    currArea = max(currArea, prevArea)

                    startI = prevI

                stack.append([startI, currH])

            while stack:
                prev = stack.pop()
                i = prev[0]
                h = prev[1]
                prevArea = (len(row) - i) * h
                currArea = max(currArea, prevArea)

            maxArea = max(maxArea, currArea)
        return maxArea