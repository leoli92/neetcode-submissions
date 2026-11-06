class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "*", "-", "/"}
        k = 0
        for c in tokens:
            if c in ops:
                b = stack.pop()
                a = stack.pop()
                if c == "+":
                    stack.append(a + b)
                if c == "-":
                    stack.append(a - b)
                if c == "*":
                    stack.append(int(a * b))
                if c == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(c))

        return stack[0]
                    
