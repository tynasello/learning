def max_activities(s, f):

    n = len(f)
    print("The following activities are selected: ", end="")
    i = 0
    print(i, end=" ")
    for x in range(1, n):
        if s[x] >= f[i]:
            print(x, end=" ")
            i = x
    print()


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
max_activities(s, f)
