class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []

        for x, y in points:
            dist = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(distance_heap, (dist, [x, y]))
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(distance_heap)[1])
        
        return res