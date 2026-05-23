''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def dfs(root):
            if not root:
                return 0
            value = root.data
            root.data = dfs(root.left) + dfs(root.right)
            return value + root.data
        dfs(root)
        