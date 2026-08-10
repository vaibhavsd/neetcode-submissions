# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorder = 0

        def func(root, k):
            nonlocal preorder
            if not root:
                return -1

            out = func(root.left, k)
            if out != -1:
                return out

            if preorder + 1 == k:
                #print(f'preorder+1- {preorder+1}')
                #print(f'k- {k}')
                #print(f'root.val- {root.val}')
                return root.val
            preorder += 1

            out = func(root.right, k)
            if out != -1:
                return out

            return -1
        return func(root, k)
