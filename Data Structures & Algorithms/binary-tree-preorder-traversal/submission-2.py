# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol= []
        def preorderTraversal2(root):
            if not root:
                return
            sol.append(root.val)
            preorderTraversal2(root.left)
            preorderTraversal2(root.right)
            return sol
        preorderTraversal2(root)
        return sol