class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        the key to solving this problem is knowing that a region can only be 
        uncapturable if one of its values is on an edge of the grid
        '''
        nrows = len(board)
        ncols = len(board[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def markRegionUncapturable(rowi, coli):
            if rowi < 0 or rowi >= nrows or coli < 0 or coli >= ncols or board[rowi][coli] != "O":
                return
            board[rowi][coli] = "*"

            for vert, horiz in directions:
                newRowi = rowi + vert
                newColi = coli + horiz
                markRegionUncapturable(newRowi, newColi)

        # mark all uncapturable regions as *
        # top
        for coli in range(ncols):
            markRegionUncapturable(0, coli)
        # bottom
        for coli in range(ncols):
            markRegionUncapturable(nrows - 1, coli)
        # left
        for rowi in range(1, nrows - 1):
            markRegionUncapturable(rowi, 0)
        # right
        for rowi in range(1, nrows - 1):
            markRegionUncapturable(rowi, ncols - 1)

        # mark capturable regions
        for rowi in range(nrows):
            for coli in range(ncols):
                if board[rowi][coli] == "O":
                    board[rowi][coli] = "X"

        # revert uncapturable back to Os
        for rowi in range(nrows):
            for coli in range(ncols):
                if board[rowi][coli] == "*":
                    board[rowi][coli] = "O"
