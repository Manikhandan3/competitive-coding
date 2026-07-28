class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        count = [0] * n
        q = []
        rooms = []
        min_room = 0
        for meet in meetings:
            while q and meet[0] > q[0][0]:
                heapq.heappush(rooms, heapq.heappop(q)[1])
                
            if q and len(q) == n:
                node = heapq.heappop(q)
                min_room = node[1]
                heapq.heappush(q, [node[0] + meet[1] - meet[0],  node[1]])
            else:
                if rooms:
                    min_room = heapq.heappop(rooms)
                    heapq.heappush(q, [meet[1] - 1,  min_room])
                else:
                    min_room = len(q)
                    heapq.heappush(q, [meet[1] - 1,  min_room])
            # print(min_room)
            count[min_room] += 1
        m = 0
        # print(count)
        for c in range(len(count)):
            if count[c] > m:
                m = count[c]
                res = c
        return res
