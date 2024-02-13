# Help from NeetCode on youtube https://www.youtube.com/watch?v=1UOPsfP85V4
# --------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        #previous groups last node
        pl = dummy
        #current groups node
        curr = dummy
        
        while True:
            #current groups last node
            cl = self.lastGroupNode(pl, k)
            #if cl null, its grouping is not of length k, so dont swtich its values
            if not cl:
                break
            
            #setup nodes to allow the connection of first node 
            #of current group to first node of next group
            prev = cl.next
            curr = pl.next
            
            for _ in range(k):
                #next node
                nn = curr.next
                #swap nodes
                curr.next = prev
                prev = curr
                curr = nn
            
            newpl = pl.next
            #connect previous groups last node to (new) first node of current group
            #cl was origanally last node of current group
            pl.next = cl
            pl = newpl
            
        return dummy.next
    
    def lastGroupNode(self, node, k):
        for i in range(k):
            if not node.next:
                return None
            node = node.next
        return node