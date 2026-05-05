class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if i == "+":
                    res = op2 + op1
                elif i == "-":
                    res = op2-op1
                elif i == "*":
                    res = op2 * op1
                elif i == "/":
                    res = int(op2/op1)
                stack.append(res)
        return stack[0]