class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        import heapq
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
        
        res = 0
        prev = float('-inf')
        cur = 0
        while minHeap:
            pop = heapq.heappop(minHeap)
            if prev + 1 == pop:
                cur += 1
            elif prev == pop:
                continue
            else:
                cur = 1
            print(cur, pop)
            res = max(res, cur)
            prev = pop
        
        return res