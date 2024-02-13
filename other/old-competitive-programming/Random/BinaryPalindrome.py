"""
Find the nth number whose binary representation is a palindrome.
"""


def solve(n):
    if n == 1:
        return 1
    n -= 1
    q = ["11"]

    while len(q) != 0:
        currq = q.pop(0)
        n -= 1
        if n == 0:
            return int(currq, 2)

        if len(currq) & 1 == 1:
            mid = currq[len(currq) // 2]
            s = currq[: len(currq) // 2] + mid + currq[len(currq) // 2 :]
            q.append(s)

        else:
            s = currq[: len(currq) // 2] + str(0) + currq[len(currq) // 2 :]
            q.append(s)
            s = currq[: len(currq) // 2] + str(1) + currq[len(currq) // 2 :]
            q.append(s)
    return 0


if __name__ == "__main__":
    ns = [3, 6, 12]
    for n in ns:
        print(solve(n))
