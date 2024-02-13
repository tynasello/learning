class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1: return s
    
        n = len(s)
        rows = [""]*numRows
        
        
        direction = -1
        i = 0

        for char in s:
            rows[i] += char
            if i==0 or i==numRows-1:
                direction*=-1
            i += direction
                
        return ''.join(rows)
