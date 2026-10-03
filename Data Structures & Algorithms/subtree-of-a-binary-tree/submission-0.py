# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = [root]
        while stack:

            node  = stack.pop()
            if node.val == subRoot.val:
                same_stack = [(node, subRoot)]

                match = True
                while same_stack:
                    n,s = same_stack.pop()
                    if not n and not s:
                        continue
                    if not n or not s or s.val!=n.val:
                        match = False
                        break
                    same_stack.append((n.left, s.left))
                    same_stack.append((n.right,s.right))

                if match:
                    return True
                
                    
                    

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
            