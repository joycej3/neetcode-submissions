# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = min(p.val,q.val)
        big = max(p.val,q.val)
        node = root
        while True:

            if big < node.val:
                node = node.left
            elif small >node.val:
                node = node.right
            else:
                return node