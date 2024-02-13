class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set()

        def search(i, j, nextCharI):
            if nextCharI == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if board[i][j] != word[nextCharI]:
                return False
            if (i, j) in visited:
                return False

            nextCharI += 1
            visited.add((i, j))
            res = (
                search(i + 1, j, nextCharI)
                or search(i - 1, j, nextCharI)
                or search(i, j + 1, nextCharI)
                or search(i, j - 1, nextCharI)
            )
            visited.remove((i, j))

            return res

        for i in range(n):
            for j in range(m):
                if search(i, j, 0):
                    return True
        return False
