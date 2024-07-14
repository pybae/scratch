from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        rotate = (length - k) % length
        if rotate == 0:
            return head

        prev, cur, i = None, head, 0
        while i < rotate:
            prev = cur
            cur = cur.next
            i += 1

        ans = cur
        prev.next = None # cut the head
        while cur.next:
            cur = cur.next
        cur.next = head

        return ans


sol = Solution()
ans = sol.rotateRight(ListNode(0, ListNode(1, ListNode(2))), 4)

while ans:
    print(ans.val, end=", ")
    ans = ans.next
print()
