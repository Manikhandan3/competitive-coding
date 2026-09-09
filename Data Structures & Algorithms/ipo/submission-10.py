class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        rev = [[c,p] for c,p in zip(capital,profits)]
        rev.sort()
        maxHeap = []
        i = 0 
        while k > 0:
            while i < len(rev) and rev[i][0] <= w:
                heapq.heappush(maxHeap, -rev[i][1])
                i += 1
            if not maxHeap:
                break
            p = heapq.heappop(maxHeap)
            w -= p
            k -= 1
        return w