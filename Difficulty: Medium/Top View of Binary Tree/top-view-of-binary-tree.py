'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        if not root:
            return []
        # code here
        right = []
        left = []
        q = deque()
        q.append((root, 0))
        while q:
            node, width = q.popleft()
            if len(left) == width:
                left.append(node.data)
            if len(right) == -width:
                right.append(node.data)
            if node.left:
                q.append((node.left, width + 1))
            if node.right:
                q.append((node.right, width - 1))
        left.reverse()
        left.pop()
        return left + right