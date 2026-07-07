
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q=deque([node])
        clone={node.val:Node(node.val)}
        while q:
            x=q.popleft()
            x_clone=clone[x.val]
            for neighbor in x.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val]=Node(neighbor.val)
                    q.append(neighbor)
                x_clone.neighbors.append(clone[neighbor.val])
        return clone[node.val]

        