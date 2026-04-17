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

