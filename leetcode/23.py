from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
So naive, is iterate and find the min each time. So what's the runtime of that?
Say n = number of lists, k = length of each list

takes O(n) to find the min
O(n^2 * k)


the merge solution is
takes O(k) to merge two lists
we have n lists
n log n, if we have 8
1 2 - 3 4 - 5 6 - 7 8 
12 34 - 56 78
1234 5678

O(nlogn * k) right?

yeah okay
"""

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            if len(lists) % 2:
                lists.append(None)
            lists = [self.mergeTwoLists(lists[i], lists[i + 1]) for i in range(0, len(lists), 2)]

        return lists[0]
    
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        while a and b:
            if a.val < b.val:
                cur.next, a = a, a.next
            else: 
                cur.next, b = b, b.next
            cur = cur.next

        if a or b:
            cur.next = a or b

        return head.next


def make_list(l: List[int]) -> ListNode:
    if not l:
        return None
    head = cur = ListNode(l[0])
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return head

def print_list(l: ListNode):
    while l:
        print(l.val, end=", ")
        l = l.next
    print()

l = make_list([1, 4, 5])
sol = Solution()
print_list(sol.mergeTwoLists(
    make_list([1, 4, 5]),
    make_list([1, 3, 4])
))

print_list(sol.mergeKLists([
    make_list([1, 4, 5]),
    make_list([1, 3, 4]),
    make_list([2, 6])
]))
print_list(sol.mergeKLists([]))
print_list(sol.mergeKLists([make_list([])]))
