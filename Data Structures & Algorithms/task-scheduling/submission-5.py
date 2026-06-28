class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)

        for t in tasks:
            count[t] += 1

        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        
        time = 0
        q = deque()
        while maxheap or q:
            time += 1

            if not maxheap:
                time = q[0][0]
            else:
                freq = heapq.heappop(maxheap) + 1
                if freq:
                    q.append([time + n, freq])
            
            if q and q[0][0] == time:
                heapq.heappush(maxheap, q.popleft()[1])
        
        return time

        