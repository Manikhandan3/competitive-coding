class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-num)
        if len(self.maxHeap)-len(self.minHeap) > 1:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if not self.minHeap:
            return float(-self.maxHeap[0])
        l = (len(self.maxHeap)+len(self.minHeap))%2
        if not l:
            return (float(-self.maxHeap[0]) + float(self.minHeap[0]))/2
        else:
            return float(-self.maxHeap[0])
        
        