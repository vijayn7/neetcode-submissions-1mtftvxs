import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        opps = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        
        numSt = []

        for token in tokens:
            if token in opps:
                b = numSt.pop()
                a = numSt.pop()
                numSt.append(opps[token](a, b))
            else:
                numSt.append(int(token))
        
        return numSt[-1]