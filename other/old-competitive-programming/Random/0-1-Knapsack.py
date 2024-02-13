def solve(capacity, i):
    if arr[i][capacity]:
        return arr[i][capacity]
    if i == 0 or capacity == 0:
        res = 0
    elif weights[i] > capacity:
        res = solve(capacity, i - 1)
    else:
        temp1 = solve(capacity, i - 1)
        temp2 = values[i] + solve(capacity - weights[i], i - 1)
        res = max(temp1, temp2)
    arr[i][capacity] = res
    return res


values = [0, 60, 100, 120]
weights = [0, 10, 20, 30]
capacity = 50

arr = [[0] * (capacity + 1) for i in range(len(weights))]
print(solve(capacity, len(weights) - 1))
