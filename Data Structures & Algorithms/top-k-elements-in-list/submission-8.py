class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for n, f in freq.items():
            bucket[f].append(n)
        
        res = []
        for buck in bucket[::-1]:
            if buck:
                res.extend(buck)
                if len(res) == k:
                    return res

