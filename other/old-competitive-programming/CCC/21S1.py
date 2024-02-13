n = int(input())
a = 0

if __name__ == "__main__":
    ls = list(map(int, input().split()))
    ws = list(map(int, input().split()))
    for i in range(n):
        a += (ls[i] + ls[i + 1]) * ws[i] / 2
    if a % int(a) == 0:
        print(int(a))
    else:
        print(a)
