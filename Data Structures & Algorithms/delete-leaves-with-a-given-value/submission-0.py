# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def godelete(root, target):
            if not root:
                return None, False
            action1= False
            action2= False

            if root.left:
                out1node, action1 = godelete(root.left, target)
                root.left= out1node
            if root.right:
                out2node, action2 = godelete(root.right, target)
                root.right= out2node
            if action1 or action2:
                return2= True
            else:
                return2= False

            if not root.left and not root.right:
                if root.val==target:
                    return1= None
                    return2= True
                else:
                    return1= root
            else:
                return1= root
            return return1, return2

            


        while True:
            outnode, action= godelete(root, target)
            root= outnode
            if not action:
                break
        
        return root