class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxheap = []
        for i, p in enumerate(position):
            heapq.heappush(maxheap, (-p, i))
        
        stack = []
        while maxheap:
            item = heapq.heappop(maxheap)
            index = item[1]
            p = -item[0]
            
            time = (target - p) / speed[index]
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)