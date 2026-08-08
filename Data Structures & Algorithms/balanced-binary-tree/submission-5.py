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
        def isBalanced2(root):
            if not root:
                return True, 0    
            left, lh= isBalanced2(root.left)
            right, rh= isBalanced2(root.right)
            if not left or not right:
                return False, -1
            if abs(lh-rh)>1:
                return False, -1
            else:
                return True, max(lh, rh)+1
        
        a, b= isBalanced2(root)
        return a

        
