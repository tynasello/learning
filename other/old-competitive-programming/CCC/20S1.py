# Find max running speed

length = int(input())
vel = []
td = []


def solve():

    for date in range(len(td) - 1):
        time1 = td[date][0]
        distance1 = td[date][1]
        time2 = td[date + 1][0]
        distance2 = td[date + 1][1]
        vel.append(abs(distance1 - distance2) / abs(time1 - time2))


if __name__ == "__main__":

    for _ in range(length):
        time, distance = map(int, input().split())
        td.append((time, distance))
    td.sort()
    solve()
    print(max(vel))

"""
3
0 100
10 120
20 50

3
0 100
20 50
10 120



5
20 -5
0 -17 
10 31 
5 -3 
30 11 
"""
