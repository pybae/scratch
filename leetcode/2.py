from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        cur = root
        carry = 0
        while l1 != None or l2 != None or carry > 0:
            result = carry 
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next

            if result >= 10:
                carry = 1
            else:
                carry = 0

            cur.val = result % 10
            if l1 != None or l2 != None or carry > 0:
                cur.next = ListNode()
                cur = cur.next

        return root

sol = Solution()

def printl(l):
    while l != None:
        print(l.val, end="")
        l = l.next
    print()

printl(sol.addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4)))))
printl(sol.addTwoNumbers(
    ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
    ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
