class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for s in strs:
            occ = [0] * 26;

            for c in s:
                occ[ord(c) - ord('a')] += 1

            key = ""
            for i in range(26):
                key += str(occ[i]) + '_'

            map[key].append(s)

        return list(map.values())
        

            
