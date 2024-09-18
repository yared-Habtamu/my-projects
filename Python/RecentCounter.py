class RecentCounter(object):
    TIME=3000

    def __init__(self):
        self.data=deque()
        

    def ping(self, t):
        self.data.append(t)
        while self.data[0] < t - self.TIME:
            self.data.popleft()
        return len(self.data)

        """
        :type t: int
        :rtype: int
        """
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
