class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        freq = Counter(s)
        maxHeap = [[-v,k] for k,v in freq.items()]
        heapq.heapify(maxHeap)
        prev = []
        while maxHeap or prev:
            if not maxHeap:
                return ""
            count, c = heapq.heappop(maxHeap)
            res += c
            if prev:
                heapq.heappush(maxHeap,[prev[1], prev[0]])
            if count < -1:
                prev = [c, count + 1]
            else:
                prev = []
        return res
