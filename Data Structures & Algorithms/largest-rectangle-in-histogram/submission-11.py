class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                item = stack.pop()
                area = (i - item[0]) * item[1]
                res = max(res, area)
                start = item[0]
            stack.append((start, h))

        length = len(heights)
        print(stack)
        while stack:
            item = stack.pop()
            area = (length - item[0]) * item[1]
            res = max(res, area)
        
        return res