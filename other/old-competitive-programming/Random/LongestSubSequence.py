def solve(arr, n):
    for k in range(n):
        length[k] = 1
        for i in range(k):
            if arr[i] < arr[k]:
                length[k] = max(length[k], length[i] + 1)
    return length


arr = [6, 2, 5, 1, 7, 4, 8, 3]
n = len(arr)
length = [0] * n
print(max(solve(arr, n)))
