class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            if not stack or t <= stack[-1][0]:
                stack.append((t, i))
                continue
                
            while stack and t > stack[-1][0]:
                _, index = stack.pop()
                res[index] = i - index 
            stack.append((t, i))

        return res