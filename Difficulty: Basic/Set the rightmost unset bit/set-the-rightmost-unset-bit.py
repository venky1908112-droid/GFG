class Solution:
    def setBit(self, n):
        # code here
        res = 0
        x = n
        done = False
        bl = n.bit_length()
        for i in range(bl):
            if n & 1:
                res |= (1 << i)
            elif not done:
                done = True
                res |= (1 << i)
            n >>= 1
        if not done:
            return x + pow(2, bl)
        return res