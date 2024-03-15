# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def sub(root,s):
            if not root:
                return
            s.append(root.val)
            sub(root.left,s)
            sub(root.right,s)
            return s
        def dfs(root):
            nonlocal res
            if not root:
                return
            t = sub(root, [])
            avg = sum(t)//len(t)
            if avg==root.val:
                res+=1
            dfs(root.left)
            dfs(root.right)
        dfs(root) 
        print(res)
        return res
        