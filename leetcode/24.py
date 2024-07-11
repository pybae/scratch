from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            next = cur.next.next 
            prev.next = cur.next
            cur.next.next = cur
            cur.next = next
            
            if cur.next:
                cur = cur.next
                prev = prev.next.next

        return dummy.next


def print_list(l):
    while l:
        print(l.val, end=" ")
        l = l.next
    print()

sol = Solution()
print_list(sol.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
print_list(sol.swapPairs(None))
print_list(sol.swapPairs(ListNode(1)))
