class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list()

        for val in zip(position, speed):
            cars.append(val)
        
        cars.sort(key = lambda x: x[0])

        st = list()

        for car in cars:

            if not st:
                st.append(car)

            while (len(st) != 0):
                top = st[-1]
                timeCurr = (target - car[0]) / car[1]
                timeTop = (target - top[0]) / top[1]

                if (timeTop > timeCurr):
                    break

                st.pop()
            
            st.append(car)

        return len(st)
                
                
