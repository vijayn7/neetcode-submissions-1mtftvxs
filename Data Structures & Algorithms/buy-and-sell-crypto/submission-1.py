class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]

        maxProf = 0

        for price in prices:
            maxProf = max(maxProf, price - minPrice)
            minPrice = min(minPrice, price)
        
        return maxProf