class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def getHash(s: str) -> tuple:
            occ = [0] * 26
            for c in s:
                occ[ord(c) - ord('a')] += 1
            
            return tuple(occ)
        
        toMatch = getHash(s1)

        for i in range(len(s2) - len(s1) + 1):
            key = getHash(s2[i:i + len(s1)])
            if toMatch == key:
                return True
        
        return False