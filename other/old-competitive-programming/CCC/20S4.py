import sys


def moves(a, b, c):
    minmove = (
        len(a) - a.count("A") + len(b) - b.count("B") - min(a.count("B"), b.count("A"))
    )

    return minmove


def solve(seats):
    lenA = 0
    lenB = 0
    lenC = 0
    for char in seats:
        if char == "A":
            lenA += 1
        elif char == "B":
            lenB += 1
        else:
            lenC += 1

    a = seats[:lenA]
    b = seats[lenA : lenA + lenB]
    c = seats[lenA + lenB :]

    ans = sys.maxsize

    for start in range(len(seats)):
        minMoves = moves(a, b, c)
        if minMoves < ans:
            ans = minMoves
        c += a[0]
        a = a[1:]
        a += b[0]
        b = b[1:]
        b += c[0]
        c = c[1:]
    return ans


if __name__ == "__main__":

    seats = input()

    ans = solve(seats)
    for i, char in enumerate(seats):
        if char == "A":
            seats = seats[:i] + "C" + seats[i + 1 :]
        elif char == "C":
            seats = seats[:i] + "A" + seats[i + 1 :]
    ans = min(ans, solve(seats))
    print(ans)
