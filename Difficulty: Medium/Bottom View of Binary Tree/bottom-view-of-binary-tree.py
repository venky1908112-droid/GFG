'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import defaultdict, deque
class Solution:
    def bottomView(self, root):
        mp = defaultdict(int)
        q = deque()
        q.append((root, 0))
        while q:
            node, width = q.popleft()
            mp[width] = node.data
            if node.left:
                q.append((node.left, width - 1))
            if node.right:
                q.append((node.right, width + 1))
        res = []
        
        for key in sorted(mp):
            res.append(mp[key])
        return res
        