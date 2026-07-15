class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # follower : followees
        self.tweetMap = defaultdict(list) # user : tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            tweets_list = self.tweetMap[user]
            if not tweets_list:
                continue
            tweet_length = len(tweets_list)
            latest_tweet_time, latest_tweet = tweets_list[-1]
            heapq.heappush(maxheap, (latest_tweet_time, user, latest_tweet, tweet_length - 1))
        
        res = []
        while maxheap and len(res) < 10:
            _, user, tweet, idx = heapq.heappop(maxheap)
            res.append(tweet)
            if idx > 0:
                next_tweet_time, next_tweet = self.tweetMap[user][idx - 1]
                heapq.heappush(maxheap, (next_tweet_time, user, next_tweet, idx - 1))
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
