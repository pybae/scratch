from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        yeah i guess the key insight here is think recursively
        preorder segments the trees, do it up like that
        i'm surprised this works though, it's some complicated assumption on preorder showing parents over children

        is it enough to compare left and right in sequence of inorder when compared to preorder?

        so the root is preorder[0]
        preorder[1] may be on the left or on the right

        if preorder[1] is on the left, then it should be on the left of the element in inorder
        why? because in order goes left, val, right, so if it were on the left, it should beleft

        likewise
        if preorder[1] is on the right, it should be on the right side

        think that works?
        so 9 is on the left

        20 is next
        what do we compare 20 to

        20 could be on the left of 9, or it could be on the right of 3
        it could also be on the right of 9

        20 is on the right of 3, indicating that 3 is the head
        so take it and iterate back?

        does this guarantee we see parents first if we're attaching?
        preorder is val, left, right

        so it'll go all the way into left and all the things here before seeing the right side
        yeah beacuse what you attach to is that. - skeptical

        okay i think this works?
        """

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        val_to_inorder_index: dict[int, int] = dict()
        val_to_nodes: dict[int, TreeNode] = { preorder[0] : root }

        for i, val in enumerate(inorder):
            val_to_inorder_index[val] = i

        for i in range(1, len(preorder)):
            val = preorder[i]
            index = val_to_inorder_index[val]

            j = index - 1
            while j >= 0 and inorder[j] not in val_to_nodes:
                j -= 1
            left_node = val_to_nodes[inorder[j]] if j >= 0 else None

            j = index + 1
            while j < len(inorder) and inorder[j] not in val_to_nodes:
                j += 1
            right_node = val_to_nodes[inorder[j]] if j < len(inorder) else None


            new_node = TreeNode(val)
            val_to_nodes[val] = new_node

            if left_node and right_node:
                if not left_node.right:
                    left_node.right = new_node
                else:
                    right_node.left = new_node
            elif left_node:
                left_node.right = new_node
            else:
                right_node.left = new_node

        return root



def print_tree(node: Optional[TreeNode]) -> None:
    q = deque([node])
    while q:
        node = q.popleft()

        print(node.val, end=", ")
        if node.left:
            q.append(node.left)
        else:
            print("None", end=", ")

        if node.right:
            q.append(node.right)
        else:
            print("None", end=", ")

    print()


sol = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# print_tree(root)
# print_tree(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))
print_tree(sol.buildTree([1,2,3], [2,3,1]))
