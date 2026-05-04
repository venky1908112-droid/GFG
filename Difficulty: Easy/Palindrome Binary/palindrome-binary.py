#User function Template for python3

class Solution:
    def isPallindrome(self, n):
        n = bin(n)[2:]
        return 1 if n == n[::-1] else 0