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
        mlist1= self.getlist(root, p.val, [])
        mlist2= self.getlist(root, q.val, [])
        print(mlist1)
        print(mlist2)

        broke= False
        for i in range(min(len(mlist1), len(mlist2))):
            if mlist1[i]==mlist2[i]:
                continue
            else:
                broke= True
                break
        
        if broke:
            return mlist1[i-1]
        else:
            return mlist1[i]



