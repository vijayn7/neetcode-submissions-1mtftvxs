class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxWater = 0

        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)

            maxWater = max(maxWater, currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater