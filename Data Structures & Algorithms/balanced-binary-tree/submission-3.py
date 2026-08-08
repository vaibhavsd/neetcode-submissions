# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getheight(self, root):
        if not root:
            return 0
        return 1 + max(self.getheight(root.left), self.getheight(root.right))



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left= self.isBalanced(root.left)
        right= self.isBalanced(root.right)
        if not left or not right:
            return False

        lh= self.getheight(root.left)
        rh= self.getheight(root.right)
        if abs(lh-rh)>1:
            return False
        else:
            return True
        
        
