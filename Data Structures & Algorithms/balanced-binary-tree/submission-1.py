# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root is None:
            return 0

        h1= self.height(root.left)
        h2= self.height(root.right)
        return 1 + max(h1, h2)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
             
        h1= self.height(root.left)
        h2= self.height(root.right)

        if abs(h1-h2)>1:
            return False
        else:
            return True
        