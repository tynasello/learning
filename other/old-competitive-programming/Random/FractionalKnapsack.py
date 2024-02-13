"""
same as 0-1 knapsack problem, however we can take fractions of weights
return max value you can carry without exceeding knapsack
"""


def solve(values, weights):
    currweight = 0
    maxval = 0
    lasti = 0
    for i, w in enumerate(weights):
        if cap - currweight - w >= 0:
            currweight += w
            maxval += values[i]
        else:
            lasti = i
            break

    left = cap - currweight
    n = weights[i] / left
    maxval += values[i] / n
    return maxval


def sort(values, weights):
    for _ in range(len(values)):
        for i in range(len(values) - 1):
            first = values[i] / weights[i]
            second = values[i + 1] / weights[i + 1]
            if second > first:
                values[i], values[i + 1] = values[i + 1], values[i]
                weights[i], weights[i + 1] = weights[i + 1], weights[i]


values = [120, 100, 60]
weights = [30, 20, 10]
cap = 50

sort(values, weights)
print(solve(values, weights))
