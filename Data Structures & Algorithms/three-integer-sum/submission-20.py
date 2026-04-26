class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        i = 0
        while i < len(nums) - 1:
            mid = i + 1
            j = len(nums) - 1
            while mid < j:
                threesum = nums[i] + nums[mid] + nums[j]
                if threesum > 0:
                    j -= 1
                    while mid < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif threesum < 0:
                    mid += 1
                    while mid < j and nums[mid] == nums[mid - 1]:
                        mid += 1
                else:
                    res.append([nums[i], nums[mid], nums[j]])
                    mid += 1
                    j -= 1
                    while mid < j and nums[mid] == nums[mid - 1]:
                        mid += 1
                    while mid < j and nums[j] == nums[j + 1]:
                        j -= 1
            i += 1
            
            while i < len(nums) - 1 and nums[i] == nums[i - 1]:
                i += 1
        return res