# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        q = []

        # heapify all nodes
        for l in lists:
            node = l
            while (node):
                q.append(node.val)
                node = node.next

        heapq.heapify(q)

        # reconstruct
        head = ListNode()
        dummy = head

        while (q):
            nextVal = heappop(q)
            head.next = ListNode(nextVal)
            head = head.next

        return dummy.next
