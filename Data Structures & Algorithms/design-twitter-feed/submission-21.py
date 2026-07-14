class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # follower : followees
        self.tweetMap = defaultdict(list) # user : tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.followMap[userId].add(userId)
        for user in self.followMap[userId]:
            feed += self.tweetMap[user]

        sortedFeed = sorted(feed, key=lambda x: x[0])
        res = []
        for i in range(10):
            if len(sortedFeed) <= i:
                break
            res.append(sortedFeed[i][1])
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
