# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getlist(self, root, k, currlist):
        if root is None:
            return None
        if k==root.val:
            currlist.append(root)
            return currlist
        elif k>root.val:
            currlist.append(root)
            mlist= self.getlist(root.right, k, currlist)
            if mlist:
                return mlist
        else:
            currlist.append(root)
            mlist= self.getlist(root.left, k, currlist)
            if mlist:
                return mlist
            

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            print('None')
            return None

        if p.val<root.val and q.val<root.val:
            out= self.lowestCommonAncestor(root.left, p, q)
            if out:
                print(out.val)
                return out
        elif p.val>root.val and q.val>root.val:
            out=  self.lowestCommonAncestor(root.right, p, q)
            if out:
                print(out.val)
                return out
        else:
            print(root.val)
            return root
        



