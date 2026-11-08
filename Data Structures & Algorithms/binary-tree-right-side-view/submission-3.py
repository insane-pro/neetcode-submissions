# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :return []
        ret=[]
        q=deque([root])
        while q:
            for _ in range(len(q)):
                x=q.popleft()
                if x.left :
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            ret.append(x.val)
        return ret

