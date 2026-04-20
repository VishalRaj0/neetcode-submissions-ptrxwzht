class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        heap = []
        for n, f in count.items():
            heapq.heappush(heap, (f, n))
        
        while True:
            if len(heap) == k:
                return [item[1] for item in heap]
            heapq.heappop(heap)
