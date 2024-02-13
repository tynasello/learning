import sys

if __name__ == "__main__":
    n = int(input())
    villages = []
    for _ in range(n):
        villages.append(int(input()))
    villages.sort()
    minimum = sys.maxsize
    for i in range(1, n - 1):
        sizel = (villages[i] - villages[i - 1]) / 2
        sizer = (villages[i + 1] - villages[i]) / 2
        size = sizel + sizer
        if size < minimum:
            minimum = size
    print(minimum)
