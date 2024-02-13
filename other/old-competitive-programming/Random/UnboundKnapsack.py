"""
Same as 0-1 Knapsack. Repition of items is allowed
"""


def solve(values, weights, capacity):
    for i in range(capacity + 1):
        for wi in range(len(weights)):
            if weights[wi] <= i:
                arr[i] = max(arr[i], arr[i - weights[wi]] + values[wi])
    return arr[capacity]


values = [60, 100, 120]
weights = [2, 3, 4]
capacity = 5

arr = [0 for i in range(capacity + 1)]

print(solve(values, weights, capacity))
