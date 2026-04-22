class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        prod = 1
        for n in nums:
            prefix.append(prod)
            prod *= n

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= prod
            prod *= nums[i]
        
        return prefix
        