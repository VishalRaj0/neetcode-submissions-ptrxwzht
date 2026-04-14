class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i, n in enumerate(nums):
            sub = target - n
            if sub in diff:
                return [diff[sub], i]
            diff[n] = i
        
        return []
