class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator

        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                val_1 = stack.pop()
                val_2 = stack.pop()
                res = ops[token](int(val_2), int(val_1))
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[-1]

