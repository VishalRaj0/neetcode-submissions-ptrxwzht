class Solution:
    def trap(self, height: List[int]) -> int:
        suffix = [0] * len(height)

        big = 0
        for i in range(len(height) - 1, -1, -1):
            big = max(big, height[i])
            suffix[i] = big

        res = 0
        big = 0
        for i in range(len(height)):
            big = max(big, height[i])
            res += min(big, suffix[i]) - height[i]
        
        return res