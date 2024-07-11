from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        first = head
        second = head

        while n > 0:
            second = second.next
            n -= 1

        if not second:
            return head.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next
        return head

def print_list(l):
    while l:
        print(l.val, end=" ")
        l = l.next

    print()
sol = Solution()
# l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# sol.removeNthFromEnd(l, 2)
# print_list(l)

l2 = ListNode(1, ListNode(2))
print_list(sol.removeNthFromEnd(l2, 2))
