# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def isSubTree(self, root1, root2):
        # code here
        def check_same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.data != root2.data:
                return False
            return check_same(root1.left, root2.left) and check_same(root1.right, root2.right)
            
        def search(root1, root2):
            q = deque()
            q.append(root1)
            while q:
                node = q.popleft()
                if node.data == root2.data:
                    if check_same(node, root2):
                        return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return False
        
        return search(root1, root2)
            
            