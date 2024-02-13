n = int(input())
runs1 = list(map(int, input().split()))
runs2 = list(map(int, input().split()))
sum1 = 0
sum2 = 0
ans = 0

for i in range(n):
    sum1 += runs1[i]
    sum2 += runs2[i]
    if sum1 == sum2:
        ans = i + 1
print(ans)
