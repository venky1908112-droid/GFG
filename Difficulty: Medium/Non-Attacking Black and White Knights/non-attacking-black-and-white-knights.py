class Solution:
    def numOfWays(self, n: int, m: int) -> int:
        # code here
        idx = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        ans = 0
        for i in range(m):
            for j in range(n):
                valid = 0
                for x, y in idx:
                    nx, ny = x + i, y + j
                    if 0 <= nx < m and 0 <= ny < n:
                        valid += 1
                ans += (n * m) - valid - 1
        return ans