class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ = defaultdict(int)

        for c in s:
            occ[c] += 1
        
        for c in t:
            occ[c] -= 1

        for k, v in occ.items():
            if v != 0:
                return False
        
        return True