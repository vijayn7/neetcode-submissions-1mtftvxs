class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getSignature(s : str):
            occ = [0] * 26

            for c in s:
                occ[ord(c) - ord('a')] += 1

            return tuple(occ)
        
        bins = defaultdict(list)

        for s in strs:
            bins[getSignature(s)].append(s)
        
        return [v for _, v in bins.items()]