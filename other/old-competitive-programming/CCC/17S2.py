n = int(input())
readings = list(map(int, input().split()))
if len(readings) == 1:
    print(*readings)
else:
    readings.sort()
    if n % 2 == 1:
        small = readings[: n // 2 + 1]
        big = readings[n // 2 + 1 :]
    else:
        small = readings[: n // 2]
        big = readings[n // 2 :]
    small.reverse()

    readings = []
    for i in range(n // 2):
        readings.append(small[i])
        readings.append(big[i])
    if n % 2 == 1:
        readings.append(small.pop())
    print(*readings)
