# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        total= 0
        def getsum(root, msum):
            nonlocal total
            if not root:
                return
            msum= msum*10+ root.val
            if not root.left and not root.right:
                print(f'root- {root.val}, msum- {msum}')
                total+=msum
                return
            left= getsum(root.left, msum)
            right= getsum(root.right, msum)

        getsum(root, 0)
        return total