"""
find the first smaller element that precedes a given element in an array.
"""


def solve(elIndex):
    stack = []
    if elIndex <= 0:
        return "No Solution"
    for i in range(elIndex + 1):
        if len(stack) == 0 or arr[i] > stack[-1][1]:
            stack.append([i, arr[i]])
        else:
            while arr[i] <= stack[-1][1]:
                stack.pop()
                if len(stack) == 0:
                    break
            stack.append([i, arr[i]])
    stack.pop()
    if len(stack) == 0:
        return "No Solution"
    res = str(stack[-1][1]) + " at index " + str(stack[-1][0])
    return res


arr = [1, 3, 4, -6, 5, -2, 3, -4, 9, 10, 6]
lastElementIndex = 7
print(solve(lastElementIndex))
