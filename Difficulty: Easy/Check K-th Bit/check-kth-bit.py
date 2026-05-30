class Solution:
    def checkKthBit(self, n, k):
        # code here
        return (n >> k) & 1