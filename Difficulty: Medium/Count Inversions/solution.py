class Solution:
    def inversionCount(self, arr):
        # Code Here
        def merge(nums, low, mid, high):
            pairs = 0
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    pairs += (mid + 1) - left
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1
            for i in range(low, high + 1):
                nums[i] = temp[i - low]
            return pairs

        def mergesort(nums, low, high):
            pairs = 0
            if low >= high:
                return 0
            mid = (low + high) // 2
            pairs += mergesort(nums, low, mid)
            pairs += mergesort(nums, mid + 1, high)
            pairs += merge(nums, low, mid, high)
            return pairs
        return mergesort(arr, 0, len(arr) - 1)
