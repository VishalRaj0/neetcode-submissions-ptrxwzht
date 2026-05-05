class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in bracket:
                if not stack:
                    return False
                if stack.pop() != bracket[c]:
                    return False
            else:
                stack.append(c)


        return stack == []
        