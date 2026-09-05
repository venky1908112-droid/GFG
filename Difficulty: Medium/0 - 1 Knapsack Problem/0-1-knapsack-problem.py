class Solution:
    def knapsack(self, cap: int, val: list[int], wt: list[int]) -> int:
        # code here
        n = len(wt)
        dp = [[0] * (cap + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, cap + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][cap]