class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = 1

        res = [0] * len(nums)

        for i in range(1, len(nums)):
            pre.append(nums[i] * pre[i - 1])
        
        for i in range(len(nums) - 1, -1, -1):
            p = pre[i - 1] if i - 1 >= 0 else 1
            res[i] = p * post
            post *= nums[i]
        
        return res