
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        nrows = len(grid)
        ncols = len(grid[0])

        def calcIslandArea(rowi, coli):
            if rowi < 0 or coli < 0 or rowi >= nrows or coli >= ncols or grid[rowi][coli] != 1:
                return 0

            grid[rowi][coli] = 0
            islandArea = 1

            islandArea += calcIslandArea(rowi - 1, coli)
            islandArea += calcIslandArea(rowi, coli - 1)
            islandArea += calcIslandArea(rowi + 1, coli)
            islandArea += calcIslandArea(rowi, coli + 1)
            return islandArea

        maxIslandArea = 0

        for rowi in range(nrows):
            for coli in range(ncols):
                if grid[rowi][coli] == 1:
                    maxIslandArea = max(
                        maxIslandArea, calcIslandArea(rowi, coli))

        return maxIslandArea
