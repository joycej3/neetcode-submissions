# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diam(self,root):
        if not root:
            return 0


        left = self.diam(root.left)
        right = self.diam(root.right)
        self.res = max(self.res, right + left)
        return 1 + max(left, right)
        


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.diam(root)
        return self.res
        