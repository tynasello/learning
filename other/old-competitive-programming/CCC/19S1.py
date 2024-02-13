square = [[1, 2], [3, 4]]
si = str(input())
hc = 0
vc = 0
for c in si:
    if c == "H":
        hc += 1
    else:
        vc += 1

if hc % 2 != 0:
    square[0], square[1] = square[1], square[0]
if vc % 2 != 0:
    square[0][0], square[0][1] = square[0][1], square[0][0]
    square[1][0], square[1][1] = square[1][1], square[1][0]
print(square[0][0], square[0][1])
print(square[1][0], square[1][1])
