from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
		# code here
		res = image.copy()
		q = deque()
		q.append((sr, sc))
		m = len(image)
		n = len(image[0])
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		curr_color = image[sr][sc]
		while q:
		    x, y = q.popleft()
		    if res[x][y] == newColor:
		        continue
		    res[x][y] = newColor
		    for dx, dy in directions:
		        nx, ny = x + dx, y + dy
		        if 0 <= nx < m and  0 <= ny < n and image[nx][ny] == curr_color and res[nx][ny] != newColor:
		            q.append((nx, ny))
	    return res
		        