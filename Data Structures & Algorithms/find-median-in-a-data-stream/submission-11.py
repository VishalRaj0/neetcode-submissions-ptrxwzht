class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap or num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        minlen = len(self.minheap)
        maxlen = len(self.maxheap)

        if minlen > maxlen:
            return self.minheap[0]
        elif minlen < maxlen:
            return - self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2
        
        