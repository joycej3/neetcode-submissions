# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:return (True, 0)

        l_bool, l_height = self.dfs(root.left)
        r_bool, r_height = self.dfs(root.right)

        if abs(r_height - l_height) > 1 or not l_bool or not r_bool:
            return(False,0)
        return (True, 1+ max(l_height,r_height)) 





    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]