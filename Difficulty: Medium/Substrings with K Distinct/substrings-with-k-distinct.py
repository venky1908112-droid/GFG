class Solution:
    def countSubstr (self, s, k):
        # Code here
        def idx(x):
            return ord(x) - 97
        sub_count = 0
        window= [0] * 26
        n = len(s)
        unique = 0
        left = 0
        for right in range(n):
            i = idx(s[right])
            if window[i] == 0:
                unique += 1
            window[i] += 1
            if unique < k:
                continue
            p = right
            t = idx(s[p])
            while p < n and window[t] > 0:
                p += 1
                if p < n:
                    t = idx(s[p])
            val = p - right
            while unique >= k:
                sub_count += val
                j = idx(s[left])
                window[j] -= 1
                if window[j] == 0:
                    unique -= 1
                left += 1
        return sub_count