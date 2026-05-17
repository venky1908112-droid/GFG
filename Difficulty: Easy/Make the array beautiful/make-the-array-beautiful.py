class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        def is_diff_sign(a, b):
            if a >= 0 and b >= 0:
                return False
            if a < 0 and b < 0:
                return False
            return True
        # code here
        stack = []
        for x in arr:
            if not stack:
                stack.append(x)
            elif is_diff_sign(stack[-1], x):
                stack.pop()
            else:
                stack.append(x)
        return stack