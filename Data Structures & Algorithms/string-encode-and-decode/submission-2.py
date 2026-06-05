class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = list()

        if len(s) == 0:
            return res

        start = 0
        i = 0

        while i < len(s):
            if s[i] == '#':
                length = int(s[start:i])
                res.append(s[i+1:i + length + 1])
                start = i + length + 1
                i = start + 1
            else:
                i += 1
        
        return res