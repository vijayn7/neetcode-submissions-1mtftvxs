class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def getHash(s: str) -> tuple:
            occ = [0] * 26

            for c in s:
                occ[ord(c) - ord('a')] += 1
            
            return tuple(occ)
        
        for s in strs:
            groups[getHash(s)].append(s)
        
        res = []

        for group in groups.values():
            res.append(group)
        
        return res