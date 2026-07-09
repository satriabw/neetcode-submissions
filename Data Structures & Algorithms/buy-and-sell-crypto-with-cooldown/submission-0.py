class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding, sold, cooldown = -prices[0], 0, 0
        for i in range(1, len(prices)):
            prev_holding = holding
            prev_sold = sold
            prev_cooldown = cooldown

            holding  = max(prev_holding, prev_cooldown - prices[i])
            sold    = prev_holding + prices[i]
            cooldown = max(prev_cooldown, prev_sold)
        
        return max(sold, cooldown)