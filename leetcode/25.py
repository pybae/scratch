from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        current = head
        for i in range(k):
            if not current:
                return head
            current = current.next

        current = head
        prev = None
        i = 0

        while current and i < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            i += 1

        head.next = self.reverseKGroup(current, k)

        return prev

sol = Solution()
node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node = sol.reverseKGroup(node, 2)

while node:
    print(node.val, end=", ")
    node = node.next
