from collections import deque
class Solution:
    def bfs(self, adj):
        # code here
        n = len(adj)
        visited = [False] * n
        q = deque()
        res = []
        q.append(0)
        while q:
            index = q.popleft()
            if visited[index]:
                continue
            res.append(index)
            visited[index] = True
            for i in range(len(adj[index])):
                if not visited[adj[index][i]]:
                    q.append(adj[index][i])
        return res