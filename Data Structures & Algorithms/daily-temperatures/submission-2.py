class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []

        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while st and st[-1][1] < temp:
                res[st[-1][0]] = i - st[-1][0]
                st.pop()
            
            st.append((i, temp))
        
        return res