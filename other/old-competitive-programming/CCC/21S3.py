import sys


def walkingTimes(pos, friends):
    time = 0
    for f in friends:
        ft = abs(pos - f[0]) - f[2]
        if ft <= 0:
            continue
        else:
            time += ft * f[1]
    return time


if __name__ == "__main__":
    n = int(input())
    friends = []
    low = sys.maxsize
    high = 0
    for _ in range(n):
        # p,w,d
        friend = list(map(int, input().split()))
        friends.append(friend)
        if friend[0] > high:
            high = friend[0]
        if friend[0] < low:
            low = friend[0]
    while low <= high:
        mid = (low + high) // 2
        timem = walkingTimes(mid, friends)
        timel = walkingTimes(mid - 1, friends)
        timer = walkingTimes(mid + 1, friends)
        if timem < timel and timem < timer:
            minTime = timem
            break
        if timem == timel or timem == timer:
            minTime = timem
            break
        if timem < timel:
            low = mid + 1
        elif timem < timer:
            high = mid - 1
    print(minTime)

"""
3
6 8 3
1 4 1
14 5 2
"""