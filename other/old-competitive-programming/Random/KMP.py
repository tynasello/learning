# KMP Substring Search
def KMP(word, string):
    l = len(word)
    ls = len(string)
    lps = [0] * l
    i = 0
    j = 1
    while i < l and j < l:
        if word[i] == word[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            i = lps[i - 1]
            j += 1
    i = 0
    j = 0
    patternStarts = []
    while j < ls:
        if word[i] == string[j]:
            j += 1
            i += 1

        if i == l:
            patternStarts.append(j - i)
            i = lps[i - 1]

        elif j < ls and word[i] != string[j]:
            if i != 0:
                i = lps[i - 1]
            else:
                j += 1
    return patternStarts


if __name__ == "__main__":
    string = "AABAACAADAABAABA"
    word = "AABA"
    patternStarts = KMP(word, string)
    if len(patternStarts) == 0:
        print("Pattern not found")
    else:
        print("Pattern found starting at index's: ", end="")
        for s in patternStarts:
            print(s, end=" ")
        print()