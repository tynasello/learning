def solve():
    s1 = input()
    s2 = input()
    chars = {}
    for c in range(len(s1)):
        if s1[c] not in chars.keys():
            chars[s1[c]] = 1
        else:
            chars[s1[c]] += 1

    for c in range(len(s1)):

        if s2[c] == "*":
            continue
        if chars.get(s2[c]) == 0 or s2[c] not in chars.keys():
            return "N"
        else:
            chars[s2[c]] -= 1
    return "A"


if __name__ == "__main__":
    print(solve())
