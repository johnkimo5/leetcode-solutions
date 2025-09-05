"""
<----> 300 seconds
recording number of hits in total
we should start removing hits if they're out of the the window
5 seconds
0 1 2 3 4

"""
class HitCounter:

    def __init__(self):
        self.window = 300
        self.hits = [0] * self.window
        self.time = [0] * self.window

    def hit(self, timestamp: int) -> None:
        time = timestamp % self.window
        if self.time[time] != timestamp:
            self.time[time] = timestamp
            self.hits[time] = 0
        self.hits[time] += 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for i in range(self.window):
            if timestamp - self.time[i] < 300:
                hits += self.hits[i]
        return hits
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)