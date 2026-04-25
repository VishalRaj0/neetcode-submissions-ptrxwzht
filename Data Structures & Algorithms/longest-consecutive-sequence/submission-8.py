class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0
        for n in numset:
            cur = 0
            m = n
            while m in numset:
                m -= 1
                cur += 1
            
            res = max(res, cur)
            
        
        return res