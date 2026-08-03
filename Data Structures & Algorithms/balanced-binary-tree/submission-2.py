# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root):
        if root is None:
            return -1
        return max(self.getHeight(root.left), self.getHeight(root.right))+ 1 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isBalanced(root.left):
            return False
        elif not self.isBalanced(root.right):
            return False
        else:
            a= self.getHeight(root.left)
            b= self.getHeight(root.right)
            if abs(a-b)>1:
                return False
            else:
                return True
        