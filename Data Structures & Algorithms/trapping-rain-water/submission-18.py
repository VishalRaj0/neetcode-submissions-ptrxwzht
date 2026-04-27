class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = [0] * len(height)

        big = 0
        for h in height:
            big = max(big, h)
            prefix.append(big)

        big = 0
        for i in range(len(height) - 1, -1, -1):
            big = max(big, height[i])
            suffix[i] = big

        print(prefix, suffix)
        res = 0
        for i in range(len(height)):
            print(i, prefix[i], suffix[i], height[i])
            res += min(prefix[i], suffix[i]) - height[i]
        
        return res