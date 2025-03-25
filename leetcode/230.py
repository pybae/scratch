from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        naive way is to dump it, and then index

        but honestly don't you need index? 
        that is, at the root, how do i know which side to iterate onto as i don't know the size of the subtree yet.
        
        yeah, i can't.
        """
        return self.to_sorted_list(root, [])[k - 1]

    def to_sorted_list(self, node: Optional[TreeNode], result: list[int]) -> list[int]:
        if not node:
            return result

        self.to_sorted_list(node.left, result)
        result.append(node.val)
        self.to_sorted_list(node.right, result)

        return result


sol = Solution()
root = TreeNode(3, TreeNode(1, TreeNode(2)), TreeNode(4))
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
