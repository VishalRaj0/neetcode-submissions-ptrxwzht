class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while q or maxHeap:
            time += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap) + 1
                if freq:
                    q.append((time + n, freq))
            else:
                time = q[0][0]
        
            if q and time == q[0][0]:
                heapq.heappush(maxHeap, q.popleft()[1])
        
        return time