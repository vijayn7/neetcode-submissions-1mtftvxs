class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = defaultdict(int)

        for num in nums:
            occ[num] += 1
        
        freqs = defaultdict(list)
        maxFreq = 0

        for num, freq in occ.items():
            maxFreq = max(maxFreq, freq)
            freqs[freq].append(num)
        
        res = []

        while len(res) < k:
            if maxFreq in freqs:
                atFreq = freqs[maxFreq]
                for val in atFreq:
                    res.append(val)
            maxFreq -= 1
        
        while len(res) > k:
            res.pop()
        
        return res