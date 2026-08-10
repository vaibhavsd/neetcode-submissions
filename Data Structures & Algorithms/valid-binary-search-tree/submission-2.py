# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def func(root, maxT, minT):
            if not root:
                return True
            if root.val>=maxT or root.val<=minT:
                return False
            
            left= func(root.left, root.val, minT)
            if not left:
                return False

            right= func(root.right, maxT, root.val)
            if not right:
                return False
            return True
            
        inf= 99999999
        out= func(root, inf, -inf)
        return out