# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        left = self.inorderTraversal(root.left)
        center= root.val
        right= self.inorderTraversal(root.right)
        total= []
        if left:
            for i in left:
                total.append(i)
        total.append(center)
        if right:
            for i in right:
                total.append(i)
        return total
