def getMax(citizens, country1, country2):
    res = 0
    for i in range(citizens):
        if country1[-1] > country2[-1]:
            res += country1.pop()
        else:
            res += country2.pop()
    return res


def getMin(citizens, country1, country2):
    res = 0
    for i in range(citizens):
        if country1[-1] > country2[-1]:
            res += country1.pop()
            country2.pop()
        else:
            res += country2.pop()
            country1.pop()

    return res


if __name__ == "__main__":
    operation = int(input())
    citizens = int(input())
    country1 = list(map(int, input().split()))
    country2 = list(map(int, input().split()))
    country1.sort()
    country2.sort()
    if operation == 1:
        print(getMin(citizens, country1, country2))
    else:
        print(getMax(citizens, country1, country2))
