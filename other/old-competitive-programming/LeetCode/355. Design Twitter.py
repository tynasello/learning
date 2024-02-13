class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        i = len(self.posts) - 1

        while len(feed) < 10 and i > -1:
            if (self.posts[i][0] == userId or self.posts[i][0] in self.users[userId]):
                feed.append(self.posts[i][1])
            i -= 1

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
