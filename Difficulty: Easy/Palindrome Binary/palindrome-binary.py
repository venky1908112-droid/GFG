class Solution:
    def isBinaryPalindrome(self, n):
        left = n.bit_length() - 1
        right = 0
        while left > right:
            if (n >> left) & 1 != (n >> right) & 1:
                return 0
            
            left -= 1
            right += 1
        return 1