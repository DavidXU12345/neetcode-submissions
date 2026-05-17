class Twitter:

    def __init__(self):
        self.userIdToTweets = defaultdict(list)
        self.followerIdToFolloweeIds = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userIdToTweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followerIdToFolloweeIds[userId].add(userId)
        for followeeId in self.followerIdToFolloweeIds[userId]:
            if followeeId not in self.userIdToTweets:
                continue
            index = len(self.userIdToTweets[followeeId]) - 1
            count, tweetId = self.userIdToTweets[followeeId][index]
            heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.userIdToTweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index - 1))
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerIdToFolloweeIds[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerIdToFolloweeIds[followerId]:
            self.followerIdToFolloweeIds[followerId].remove(followeeId)
