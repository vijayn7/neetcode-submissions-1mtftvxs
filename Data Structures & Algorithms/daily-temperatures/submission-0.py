class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = list()

        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while st and st[-1][0] < temperatures[i]:
                res[st[-1][1]] = i - st[-1][1]
                st.pop()
            
            st.append( (temperatures[i], i) )

        return res


        