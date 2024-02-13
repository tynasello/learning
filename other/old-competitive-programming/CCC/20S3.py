# needle permutations and haystack
n = str(input())
h = str(input())
needle_freq = {}
curr_freq = {}
used = []


def solve(s, start, finish, res):
    if finish == len(h) + 1:
        return res
    small = s[start:finish]
    if small not in used and curr_freq == needle_freq:
        res += 1
        used.append(small)
    print(curr_freq.get(s[start]))
    curr_freq[s[start]] = curr_freq.get(s[start]) - 1
    if s[finish + 1] in curr_freq:
        curr_freq[s[finish + 1]] = curr_freq.get(s[finish + 1]) + 1
    else:
        curr_freq[s[finish + 1]] = 1

    return solve(s, start + 1, finish + 1, res)


if __name__ == "__main__":
    print(n)
    for i in n:
        if i in needle_freq:
            needle_freq[i] = needle_freq.get(i) + 1
        else:
            needle_freq[i] = 1
    for i in range(len(n)):
        if h[i] in curr_freq:
            curr_freq[h[i]] = curr_freq.get(h[i]) + 1
        else:
            curr_freq[h[i]] = 1
    print(solve(h, 0, len(n), 0))


"""
aab
abacabaa

aab
"""
