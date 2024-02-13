class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        canSegment = [0] * (n + 1)
        canSegment[n] = 1
        # where canSegment[i] holds boolean of wether or not we can correctly
        # segment s from index i on.

        for i in range(n-1, -1, -1):
            for word in wordDict:
                lw = len(word)
                if(lw>n-i): continue
                if(canSegment[i+lw] and s[i:i+lw] == word):
                    canSegment[i] = 1
                    break
        
        return canSegment[0]