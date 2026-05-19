class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i < j:
            m = (i + j) // 2
            if nums[j] < nums[m]:
                i = m + 1
            else:
                j = m 

        cut = i
        i = 0
        j = len(nums) - 1
        if nums[cut] <= target <= nums[j]:
            i = cut
        else:
            j = cut

        while i <= j:
            m = (i + j) // 2
            if nums[m] > target:
                j = m - 1
            elif nums[m] < target:
                i = m + 1
            else:
                return m
        return -1
            