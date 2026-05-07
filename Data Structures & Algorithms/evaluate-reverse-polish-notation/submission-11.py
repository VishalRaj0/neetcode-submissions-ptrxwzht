class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", '-', '/', '*'}

        for val in tokens:
            if val in symbols:
                num2 = stack.pop()
                num1 = stack.pop()

                res = int(eval(f"{num1} {val} {num2}"))
                stack.append(res)
            else:
                stack.append(val)
        
        return int(stack[-1]) if stack else 0
