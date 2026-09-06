class Solution:
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [False] * n
        res = []
        def dffs(index):
            if visited[index]:
                return
            res.append(index)
            visited[index] = True

            for i in range(len(adj[index])):
                dffs(adj[index][i])
        dffs(0)
        return res