class Solution:
    def replaceElements(self, arr):
        n = len(arr)

        if n == 1:
            return arr

        temp = arr[:] 

        for i in range(n):
            if i == 0:
                arr[i] = temp[i] ^ temp[i + 1]
            elif i == n - 1:
                arr[i] = temp[i - 1] ^ temp[i]
            else:
                arr[i] = temp[i - 1] ^ temp[i + 1]

        return arr