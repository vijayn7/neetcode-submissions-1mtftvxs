class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = defaultdict(int) 

        for i, n in enumerate(nums):
            corsponding = target - n

            if corsponding in pair:
                return [pair[corsponding], i]
            else:
                pair[n] = i
        
        return []