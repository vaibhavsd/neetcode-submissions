# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        from collections import deque
        sol= defaultdict(int)

        def func(root, level):
            
            myq= deque()
            myq.append((root, level))

            while myq:
                topnode, lev= myq.popleft()
                if topnode:
                    sol[lev]= topnode.val
                    myq.append((topnode.left, lev+1))
                    myq.append((topnode.right, lev+1))
        
        
        func(root, 0)
        # do something now
        return list(sol.values())
        





