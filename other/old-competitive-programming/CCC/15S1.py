if __name__ == "__main__":
    n = int(input())
    ans = 0
    nums = []
    for _ in range(n):
        num = int(input())
        if num == 0:
            ans -= nums.pop()
        else:
            nums.append(num)
            ans += num
    print(ans)