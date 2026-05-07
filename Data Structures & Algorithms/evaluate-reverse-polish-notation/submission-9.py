class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {"+", '-', '/', '*'}

        for val in tokens:
            if val in symbols:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if val == '+':
                    res = num1 + num2
                elif val == '-':
                    res = num1 - num2
                elif val == '*':
                    res = num1 * num2 
                else:
                    res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(val)
        
        return int(stack[-1]) if stack else 0
