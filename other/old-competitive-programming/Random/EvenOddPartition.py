"""
Given a singly linked list, arrange the nodes such that all even index nodes appear before the odd index nodes.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()


def solve(head):

    if head is None or head.next is None:
        return head

    dummyeven = Node(-1)
    dummyodd = Node(-1)

    eventail = dummyeven
    oddtail = dummyodd

    index = 0
    curr = head
    while curr != None:
        if index % 2 == 0:
            eventail.next = curr
            eventail = curr
        else:
            oddtail.next = curr
            oddtail = curr
        if curr is None:
            continue
        curr = curr.next
        index += 1

    eventail.next = dummyodd.next
    oddtail.next = None
    dummyeven = dummyeven.next
    while dummyeven:
        print(dummyeven.val, end=" ")
        dummyeven = dummyeven.next
    print()


# create linked list
linkli = LinkedList()
for n in range(20):
    linkli.insert(n)
print("Unarranged", end=" ")
linkli.print()
print("Arranged", end="   ")
solve(linkli.head)
