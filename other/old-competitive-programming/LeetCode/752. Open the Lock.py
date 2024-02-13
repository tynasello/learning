class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        deadends = {"0000"}.union(deadends)

        q = deque()
        # [code, num moves to get to code]
        q.append(["0000", 0])

        while (q):
            code, moves = q.popleft()
            if (code == target):
                return moves
            for i, char in enumerate(code):
                up = code[:i] + str((int(char) + 1) % 10) + code[i+1:]
                down = code[:i] + str((int(char) + 9) % 10) + code[i+1:]
                if (up not in deadends):
                    q.append([up, moves + 1])
                    deadends.add(up)
                if (down not in deadends):
                    q.append([down, moves + 1])
                    deadends.add(down)

        return -1
