class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for n in stones:
            heapq.heappush(heap, -n) # max heap
        
        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            diff = abs(s1 - s2)
            if diff:
                heapq.heappush(heap, -diff)
        
        return -heap[0] if heap else 0