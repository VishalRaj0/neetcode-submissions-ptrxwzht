class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-n for n in nums]
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        popped_vals = []
        for i in range(self.k):
            popped_vals.append(heapq.heappop(self.nums))

        for val in popped_vals:
            heapq.heappush(self.nums, val)
        
        return -popped_vals[-1]
