class Twitter:

    def __init__(self):
        self.follower_to_followees = defaultdict(set)
        self.user_to_count_tweet_ids = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # count is to serve as timestamp and differentiate the order of tweets between different users
        self.count += 1
        self.user_to_count_tweet_ids[userId].append((-self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower_to_followees[userId].add(userId)
        max_heap = []
        for followee in self.follower_to_followees[userId]:
            for cnt, tweet_id in self.user_to_count_tweet_ids[followee]:
                heapq.heappush(max_heap, (cnt, tweet_id))
        res = []
        # print(max_heap)
        while max_heap and len(res) < 10:
            res.append(heapq.heappop(max_heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_to_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_to_followees[followerId]:
            self.follower_to_followees[followerId].remove(followeeId)
        
