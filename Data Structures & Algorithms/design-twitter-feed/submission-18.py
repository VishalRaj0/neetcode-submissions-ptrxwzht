from datetime import datetime
class Twitter:

    def __init__(self):
        self.followees = defaultdict(set) # user : [followees]
        self.tweets = defaultdict(list) # user: [(count, tweet)]
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        self.followees[userId].add(userId)
        for user in self.followees[userId]:
            for tweetobj in self.tweets[user]:
                heapq.heappush(minheap, tweetobj)
                if len(minheap) > 10:
                    heapq.heappop(minheap)
                    
        minheap = sorted(minheap, key=lambda x: x[0], reverse=True)
        return [tweet for _, tweet in minheap]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followees[followerId]:
            return
        self.followees[followerId].remove(followeeId)
