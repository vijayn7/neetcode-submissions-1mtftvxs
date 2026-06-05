class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = list()

        for t in tokens:
            if t == '+':
                v1 = nums.pop()
                v2 = nums.pop()
                nums.append(v2 + v1)
            elif t == '-':
                v1 = nums.pop()
                v2 = nums.pop()
                nums.append(v2 - v1)
            elif t == '*':
                v1 = nums.pop()
                v2 = nums.pop()
                nums.append(v2 * v1)
            elif t == '/':
                v1 = nums.pop()
                v2 = nums.pop()
                nums.append(int(v2 / v1))
            else:
                nums.append(int(t))
        
        return nums[-1]