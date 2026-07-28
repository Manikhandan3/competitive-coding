class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n
        q = []
        rooms = list(range(n))
        heapq.heapify(rooms)
        time = meetings[0][0]
        for s,e in meetings:
            time = q[0][0] if not rooms else max(time,s)
            while q and time >= q[0][0]:
                heapq.heappush(rooms, heapq.heappop(q)[1])
            
            min_room = heapq.heappop(rooms)
            count[min_room] += 1
            print(min_room)
            heapq.heappush(q, [time + e - s,  min_room])
            # if q and len(q) == n:
            #     node = heapq.heappop(q)
            #     min_room = node[1]
            #     heapq.heappush(q, [node[0] + meet[1] - meet[0],  node[1]])
            # else:
            #     if rooms:
            #         min_room = heapq.heappop(rooms)
            #         heapq.heappush(q, [meet[1] - 1,  min_room])
            #     else:
            #         min_room = len(q)
            #         heapq.heappush(q, [meet[1] - 1,  min_room])
        m = 0
        # print(count)
        for c in range(len(count)):
            if count[c] > m:
                m = count[c]
                res = c
        return res
