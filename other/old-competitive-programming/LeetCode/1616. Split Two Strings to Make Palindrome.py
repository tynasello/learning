class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        
        n = len(a)
        if a[::-1] == a or b[::-1] == b: return True
        
        
        i = 0
        while a[i]==b[n-1-i] and i<n//2:
            i+=1
            
        pals = [
            a[:i]+b[i:],
            a[:n-i]+b[n-i:]
        ]
        
        for pal in pals:
            if (pal==pal[::-1]):
                return True

        # ---
        
        i = 0
        while b[i]==a[n-1-i]:
            i+=1
            
        pals = [
            b[:i]+a[i:],
            b[:n-i]+a[n-i:]
        ]
        
        for pal in pals:
            if (pal==pal[::-1]):
                return True
            
        return False
        