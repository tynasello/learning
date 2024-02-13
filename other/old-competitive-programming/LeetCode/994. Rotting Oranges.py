class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        def canBecomeRotten(rowi, coli):
            if rowi < 0 or rowi >= nrows or coli < 0 or coli >= ncols or grid[rowi][coli] != 1:
                return False
            return True

        numFreshOranges = 0
        rottenOranges = deque()
        minTime = 0

        for rowi in range(nrows):
            for coli in range(ncols):
                if grid[rowi][coli] == 1:
                    numFreshOranges += 1
                elif grid[rowi][coli] == 2:
                    rottenOranges.append((rowi, coli))

        while rottenOranges and numFreshOranges > 0:
            minTime += 1

            for _ in range(len(rottenOranges)):
                print(rottenOranges)
                rottenOrangeRowi, rottenOrangeColi = rottenOranges.popleft()
                print(rottenOranges)

                if canBecomeRotten(rottenOrangeRowi - 1, rottenOrangeColi):
                    numFreshOranges -= 1
                    grid[rottenOrangeRowi - 1][rottenOrangeColi] = 2
                    rottenOranges.append(
                        (rottenOrangeRowi - 1, rottenOrangeColi))

                if canBecomeRotten(rottenOrangeRowi, rottenOrangeColi - 1):
                    numFreshOranges -= 1
                    grid[rottenOrangeRowi][rottenOrangeColi - 1] = 2
                    rottenOranges.append(
                        (rottenOrangeRowi, rottenOrangeColi - 1))

                if canBecomeRotten(rottenOrangeRowi + 1, rottenOrangeColi):
                    numFreshOranges -= 1
                    grid[rottenOrangeRowi + 1][rottenOrangeColi] = 2
                    rottenOranges.append(
                        (rottenOrangeRowi + 1, rottenOrangeColi))

                if canBecomeRotten(rottenOrangeRowi, rottenOrangeColi + 1):
                    numFreshOranges -= 1
                    grid[rottenOrangeRowi][rottenOrangeColi + 1] = 2
                    rottenOranges.append(
                        (rottenOrangeRowi, rottenOrangeColi + 1))

        if numFreshOranges == 0:
            return minTime
        return -1
