class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        length = 0

        for n in nums:
            if (n - 1) not in s:
                curr = 1
                while (n + curr) in s:
                    curr += 1
                length = max(length, curr)

        return length