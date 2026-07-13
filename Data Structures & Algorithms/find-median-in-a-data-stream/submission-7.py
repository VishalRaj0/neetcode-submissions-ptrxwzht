class MedianFinder:

    def __init__(self):
        self.maxheap = [] # left
        self.minheap = [] # right

    def addNum(self, num: int) -> None:
        if not self.minheap or num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        
        if abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            elif len(self.maxheap) > len(self.minheap):
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        
        print(self.maxheap, self.minheap)
            
    def findMedian(self) -> float:
        # print(self.maxheap, self.minheap)
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            if len(self.minheap) > len(self.maxheap):
                return self.minheap[0]
            else:
                return -self.maxheap[0]
        