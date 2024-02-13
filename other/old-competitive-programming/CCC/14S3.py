from collections import deque


def solve(cars, N):
    branch = deque()
    need = 1
    while True:
        if need == N + 1:
            return "Y"
        if len(branch) != 0:
            if branch[0] == need:
                branch.popleft()
                need += 1
                continue
        if len(cars) != 0:
            first = cars.pop()
            if first == need:
                need += 1
                continue
            else:
                branch.appendleft(first)
        if len(cars) == 0:
            return "N"


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        cars = []
        N = int(input())
        for _ in range(N):
            cars.append(int(input()))
        print(solve(cars, N))
