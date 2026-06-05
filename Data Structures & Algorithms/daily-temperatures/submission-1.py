class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[0] * len (temp)
        stack=[]

        for i, d in enumerate(temp):
            while stack and d>stack[-1][0]:
                STd, STi = stack.pop()
                res[STi]=(i-STi)
            stack.append([d, i])
        return res         