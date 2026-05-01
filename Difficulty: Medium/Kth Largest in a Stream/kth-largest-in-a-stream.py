import heapq
class Solution:
    def kthLargest(self, arr, k):
        heap = []
        res = []
        for n in arr:
            heapq.heappush(heap, n)
            
            if len(heap) < k:
                res.append(-1)
                continue
            
            if len(heap) > k:
                heapq.heappop(heap)
            
            res.append(heap[0])
        return res