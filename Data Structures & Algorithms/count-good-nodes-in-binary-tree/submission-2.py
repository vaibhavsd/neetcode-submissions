# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        sol= [] 

        def func(root, maxval):
            if not root:
                return
            if root.val>=maxval:
                maxval= root.val
                sol.append(maxval)
                # print(f'Appended {maxval}')
            func(root.left, maxval)
            func(root.right, maxval)


        func(root, -200)
        return len(sol)