# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diaheight(root):
            if root is None:
                return 0, -1
            if root.left:
                leftdia, leftheight= diaheight(root.left)
            else:
                leftdia= 0
                leftheight= 0
            if root.right:
                rightdia, rightheight= diaheight(root.right)
            else:    
                rightdia= 0
                rightheight= 0
            dia= max(leftdia, rightdia, leftheight+rightheight)
            height= 1+ max(leftheight, rightheight)
            print(f'Returning {dia},{height} for {root.val}')
            return (dia, height)


        dia, height= diaheight(root)
        return dia
        

