from math import sqrt

n = int(input())
nums = []


def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(n):
        nums.append(int(input()))
    for num in nums:
        for i in range(2, num):
            if isPrime(i) and isPrime(num * 2 - i):
                print(i, num * 2 - i)
                break


"""
4
8
4
7
21
"""