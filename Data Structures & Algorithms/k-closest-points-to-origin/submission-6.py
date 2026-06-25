class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []

        for x, y in points:
            heapq.heappush(
                distance_heap, 
                (
                    math.sqrt((x)**2 + (y)**2), 
                    [x, y]
                )
            )
        
        return [heapq.heappop(distance_heap)[1] for i in range(k)]