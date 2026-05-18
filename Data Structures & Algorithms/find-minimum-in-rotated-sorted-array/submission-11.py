class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = nums[0]

        while i <= j:
            if nums[i] < nums[j]:
                res = min(res, nums[i])
                break

            m = (i + j) // 2
            res = min(res, nums[m])
            if nums[i] > nums[m] or nums[m] < nums[j]:
                j = m - 1
            else:
                i = m + 1

        return res