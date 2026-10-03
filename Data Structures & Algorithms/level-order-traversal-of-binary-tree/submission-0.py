# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_number = 1 
        res = []
        

        q = [root]
        while q:
            curr_level = []
            for i in range (len(q)):
                n = q.pop(0)
                curr_level.append(n.val)
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            res.append(curr_level)
        return res
            
            

    
