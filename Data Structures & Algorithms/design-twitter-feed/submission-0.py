from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                heapq.heappush(heap, (-time, tweetId))

        result = []

        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)