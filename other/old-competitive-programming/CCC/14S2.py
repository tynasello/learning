def solve():
    n = int(input())
    names = list(input().split())
    partners = list(input().split())

    pairs = []

    for i in range(n):
        first = names[i]
        second = partners[i]
        if first == second:
            return "bad"
        ind = names.index(second)
        if partners[ind] != first:
            return "bad"
    return "good"


if __name__ == "__main__":
    print(solve())