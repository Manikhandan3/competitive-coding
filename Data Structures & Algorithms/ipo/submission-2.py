class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        maxP = []
        for p,c in zip(profits,capital):
            heapq.heappush(maxHeap,[-p,c])
        for _ in range(k):
            while maxP and maxP[0][0]<=w:
                c,p = heapq.heappop(maxP)
                heapq.heappush(maxHeap,[p,c])
            while maxHeap and maxHeap[0][1] > w:
                p,c = heapq.heappop(maxHeap)
                heapq.heappush(maxP,[c,p])
            if not maxHeap:
                return w
            w = w - heapq.heappop(maxHeap)[0]
        return w
