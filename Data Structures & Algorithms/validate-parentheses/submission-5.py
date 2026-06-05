class Solution:
    def isValid(self, s: str) -> bool:
        st = list()

        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c);
            else:
                if len(st) == 0:
                    return False
                back = st[-1]
                if c == ')' and back == '(':
                    st.pop()
                elif c == '}' and back == '{':
                    st.pop()
                elif c == ']' and back == '[':
                    st.pop()
                else:
                    return False
        
        if len(st) != 0:
            return False
        return True;
                    
