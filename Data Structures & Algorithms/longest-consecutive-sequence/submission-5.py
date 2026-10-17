class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)

        longest = 1;

        if not len(nums):
            return 0

        for n in nums:
            if n - 1 not in vals:
                curr = 1
                while n + 1 in vals:
                    curr += 1
                    vals.remove(n + 1)
                    n += 1
                longest = max(longest, curr)
        
        return longest