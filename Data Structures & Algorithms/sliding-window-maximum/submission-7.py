class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxheap = []

        for j in range(k):
            heapq.heappush(maxheap, (-nums[j], j))
        
        res.append(-maxheap[0][0])

        i = 0
        for j in range(k, len(nums)):
            heapq.heappush(maxheap, (-nums[j], j))
            i += 1
            while not(i <= maxheap[0][1] <= j):
                heapq.heappop(maxheap)
            
            res.append(-maxheap[0][0])
        
        return res
        

            
            




