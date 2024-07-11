from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = head
        cur = head

        while k > 0 and cur:
            cur = cur.next
            k -= 1

        if not cur:
            # k == n, reverse the list wholly
            return self.reverse(prev, cur)

        #iterate through with some pointer and reverse shit..

        return head

    def reverse(self, prev, cur) -> Optional[ListNode]:
        node = None
        while prev:
            temp = prev.next
            prev.next = node
            node = prev
            prev = temp

        return node



def printl(l):
    while l:
        print(l.val, end="")
        l = l.next
    print()

sol = Solution()
printl(sol.reverse(ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                                                ListNode(5))))),
                   None))
printl(sol.reverseKGroup(ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                                                                      ListNode(5))))),
                         2))
