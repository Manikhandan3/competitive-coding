class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followerMap[userId].add(userId)
        if len(self.followerMap[userId]) > 10:
            maxHeap = []
            for user in self.followerMap[userId]:
                index = len(self.tweetMap[user])-1
                cnt, tweetId = self.tweetMap[user][index]
                heapq.heappush(maxHeap, [-cnt, tweetId, user, index - 1])
                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
            while maxHeap:
                cnt, tweetId, user, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-cnt, tweetId, user, index])
        else:
            for user in self.followerMap[userId]:
                if user in self.tweetMap:
                    index = len(self.tweetMap[user])-1
                    cnt, tweetId = self.tweetMap[user][index]
                    heapq.heappush(minHeap, [cnt, tweetId, user, index - 1])
        
        while minHeap and len(res) < 10:
            cnt, tweetId, userId, nxt = heapq.heappop(minHeap)
            res.append(tweetId)
            if nxt >= 0:
                cnt, tweetId = self.tweetMap[userId][nxt]
                heapq.heappush(minHeap, [cnt, tweetId, userId, nxt - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)

