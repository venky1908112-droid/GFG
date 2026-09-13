from collections import deque
class Solution:
    def countIslands(self, grid):
        islands = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'L' and not visited[i][j]:
                    islands += 1
                    q = deque()
                    q.append((i, j))
                    while q:
                        x, y = q.popleft()
                        if visited[x][y]:
                            continue
                        visited[x][y] = True
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 'L' and not visited[nx][ny]:
                                q.append((nx, ny))
        return islands