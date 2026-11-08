# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxr=float('-inf')
        def dfs(root):
            nonlocal maxr
            if not root:return 0
            l=max(dfs(root.left),0)
            r=max(dfs(root.right),0)
            maxr=max(maxr,l+r+root.val)
            return root.val+max(l,r)
        dfs(root)
        return maxr
        