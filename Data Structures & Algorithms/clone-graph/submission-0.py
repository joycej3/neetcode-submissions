"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        res = {}
        res[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()
            for neigh in curr.neighbors:
                if neigh not in res:
                    res[neigh] = Node(neigh.val)
                    q.append(neigh)
                res[curr].neighbors.append(res[neigh])
            


        return res[node]

            
