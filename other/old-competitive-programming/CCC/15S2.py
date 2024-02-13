if __name__ == "__main__":
    numJerseys = int(input())
    numAthletes = int(input())
    jerseys = []
    ans = 0
    for i in range(numJerseys):
        jerseys.append(input())
    for i in range(numAthletes):
        size, num = input().split()
        num = int(num)
        if jerseys[num - 1] != "*":
            if size == "S":
                ans += 1
                jerseys[num - 1] = "*"
            if size == "M" and jerseys[num - 1] != "S":
                ans += 1
                jerseys[num - 1] = "*"
            elif size == "L" and jerseys[num - 1] == "L":
                ans += 1
                jerseys[num - 1] = "*"
    print(ans)
