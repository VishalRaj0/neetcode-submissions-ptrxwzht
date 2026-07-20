class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.sum = 0

        def dfs(i):
            if i >= len(nums):
                return
                
            if self.sum < target:
                subset.append(nums[i])
                self.sum += nums[i]
                dfs(i)

                self.sum -= subset.pop()
                dfs(i + 1)

            elif self.sum == target:
                res.append(subset.copy())
                return
        
        dfs(0)
        return res
