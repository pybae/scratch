from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        result = cur
        while a or b:
            if not a:
                cur.next = b
                b = b.next
            elif not b:
                cur.next = a
                a = a.next
            elif a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next

        return result.next
