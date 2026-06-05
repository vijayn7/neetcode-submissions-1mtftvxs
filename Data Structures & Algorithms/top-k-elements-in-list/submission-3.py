class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = defaultdict(int)

        for x in nums:
            occ[x] += 1

        freq = defaultdict(list)

        for item, oc in occ.items():
            freq[oc].append(item)

        res = list()

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        