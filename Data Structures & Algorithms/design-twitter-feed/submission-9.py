class Twitter:
    import heapq

    def __init__(self):
        self._tweets = []
        self._follows = {}
        self._counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Fan out to followers including self
        heapq.heappush_max(self._tweets, (self._counter, (tweetId, userId)))
        self._counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        buffer = []
        self._follows.setdefault(userId, set([userId]))
        
        while len(feed) < 10 and self._tweets:
            counter, tweet = heapq.heappop_max(self._tweets)
            buffer.append((counter, (tweet[0], tweet[1])))
            if tweet[1] in self._follows.get(userId, set()):
                feed.append(tweet[0])
        
        for data in buffer:
            heapq.heappush_max(self._tweets, data)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self._follows.setdefault(followerId, set([followerId]))
        self._follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self._follows[followerId]: return
        self._follows[followerId].remove(followeeId)
