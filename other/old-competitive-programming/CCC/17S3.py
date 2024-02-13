boardValue = [0] * 2001
n = int(input())
input_ = list(map(int, input().split()))
for l in input_:
    boardValue[l] += 1
fenceHeights = [0] * 4001

for h1 in range(2000):
    for h2 in range(h1, 2001):
        if h1 == h2:
            fenceHeights[h1 + h2] += boardValue[h1] // 2
        else:
            fenceHeights[h1 + h2] += min(boardValue[h1], boardValue[h2])

longestLength = 0
numHeights = 0

for length in fenceHeights:
    if length > longestLength:
        longestLength = length
        numHeights = 1
    elif length == longestLength:
        numHeights += 1
print(longestLength, numHeights)
