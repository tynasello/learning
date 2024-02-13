class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        # removed holds removed indicies of s
        def solve(s,p,removed):
            # i will traverse s, j will traverse p
            i,j = 0,0
            # Once i or j goes out of bounds, our while loop terminates
            # Loop until out of range, or all chars in p have been found in a subsequence of s
            while i<len(s) and j<len(p):
                # We still need to find char of p at index j in s, so add 1 to i
                if i in removed or s[i]!=p[j]:
                    i+=1
                # Either the two chars matched and we can advance i and j or char of s at index i was removed so we cant match it anyways.
                else: 
                    i+=1;
                    j+=1;
            # j==len(p) represents if we were able to find a subsequence of s equal to p
            return j==len(p)
        
        # Binary search improves time complexity from O(nk) to O(nlogk) where n is len of s and k is len of removable
        # Left and right pointers
        l,r = 0,len(removable)-1
        ans = 0
        while l<=r:
            mid = (l+r)//2
            # Add all indexes of removable up until mid+1 to removed set
            removed = set(removable[:mid+1])
            # If True update ans and advance l
            if solve(s,p,removed):
                # mid+1 is the ammount of chars we were able to remove from s and still find a subsequence equal to p in it
                ans = max(ans,mid+1)
                l = mid+1
            # else False so decrement r
            else:
                r = mid-1
        return ans
    