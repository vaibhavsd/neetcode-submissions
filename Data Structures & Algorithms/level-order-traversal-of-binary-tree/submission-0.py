# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        sol= defaultdict(list)

        def func(root, level):
            if not root:
                return

            sol[level].append(root.val)
            func(root.left, level+1)
            func(root.right, level+1)

        

        func(root, 0)
        return list(sol.values())
