# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        def dfs(root):
            if not root:
                return 
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val] = 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = []
        m = 0
        print(d)
        for i in d:
            m = max(m,d[i])
        for i in d:
            if d[i]>=m:
                res.append(i)
        return res