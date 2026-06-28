# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isidentical(self, root, subRoot):
        if root is not None and subRoot is None:
            return False
        if root is None and subRoot is not None:
            return False
        if root is None and subRoot is None:
            return True
        if root.val== subRoot.val:
            if self.isidentical(root.left, subRoot.left):
                if self.isidentical(root.right, subRoot.right):
                    print(f"All matched- {root.val}, {subRoot.val}")
                    return True
        else:
            return False

        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            print(f"No subTree")
            return True
        
        if root is None and subRoot is not None:
            return False
        
        if self.isidentical(root, subRoot):
            print(f"Identical {root.val}, {subRoot.val}")
            return True
        elif self.isSubtree(root.left, subRoot):
            print(f"Matched 1 {root.left.val}, {subRoot.val}")
            return True
        elif self.isSubtree(root.right, subRoot):
            print(f"Matched 2 {root.right.val}, {subRoot.val}")
            return True
        else:
            return False