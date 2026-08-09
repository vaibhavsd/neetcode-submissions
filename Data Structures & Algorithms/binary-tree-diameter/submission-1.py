# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def func(root):
            if not root:
                return 0, 0

            ht1, dia1= func(root.left)
            ht2, dia2= func(root.right)
            
            dia= ht1+ ht2
            maxdia= max(dia, dia1, dia2)
            return 1+max(ht1, ht2), maxdia
        
        ht, dia= func(root)
        return dia
