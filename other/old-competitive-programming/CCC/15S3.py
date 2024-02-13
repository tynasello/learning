def solve(p, taken):
    ans = 0
    for _ in range(p):
        limit = int(input())
        for i in range(limit, -1, -1):
            if i == 0:
                return ans
            if taken[i] == 0:
                ans += 1
                taken[i] = 1
                break
    return ans


if __name__ == "__main__":
    g = int(input())
    p = int(input())
    taken = [0] * (g + 1)
    print(solve(p, taken))
